"""Fail-closed GitHub API 403 diagnostics; no network or secrets."""
import io
import unittest
from urllib.error import HTTPError
from unittest.mock import patch

from sync import GitHubAPI, describe_github_http_failure


def http_error(status, message, headers=None):
    return HTTPError(
        "https://api.github.com/repos/hibi89/example/contents/x?ref=main",
        status,
        "synthetic test error",
        headers or {},
        io.BytesIO(message.encode("utf-8")),
    )


class DiagnosticsTest(unittest.TestCase):
    def test_access_denied_classified_without_echoing_message(self):
        err = http_error(403, "Resource not accessible by integration secret_marker")
        kind, detail = describe_github_http_failure(err, "/repos/hibi89/example/contents/x?ref=private_marker")
        self.assertEqual(kind, "APP_ACCESS_DENIED")
        self.assertNotIn("secret_marker", detail)
        self.assertNotIn("private_marker", detail)
        self.assertIn("/repos/hibi89/example/contents/x", detail)

    def test_primary_rate_exhausted_fails_without_retry(self):
        err = http_error(403, "API rate limit exceeded", {"X-RateLimit-Remaining": "0"})
        with patch("sync.urlopen", side_effect=err) as call, patch("sync.time.sleep") as sleep:
            with self.assertRaisesRegex(RuntimeError, "PRIMARY_RATE_LIMIT"):
                GitHubAPI().get("/repos/hibi89/example/contents/README.md", "fixture-secret")
        self.assertEqual(call.call_count, 1)
        sleep.assert_not_called()

    def test_secondary_403_retries_once_after_explicit_classification(self):
        err = http_error(403, "You have exceeded a secondary rate limit", {"Retry-After": "2"})
        with patch("sync.urlopen", side_effect=[err, io.BytesIO(b'{"ok": true}')]) as call, patch("sync.time.sleep") as sleep:
            self.assertEqual(GitHubAPI().get("/repos/hibi89/example/contents/README.md", "fixture-secret"), {"ok": True})
        self.assertEqual(call.call_count, 2)
        sleep.assert_called_once_with(1)

    def test_unclassified_403_never_retries(self):
        err = http_error(403, "Forbidden unrelated test")
        with patch("sync.urlopen", side_effect=err) as call, patch("sync.time.sleep") as sleep:
            with self.assertRaisesRegex(RuntimeError, "FORBIDDEN_UNCLASSIFIED"):
                GitHubAPI().get("/repos/hibi89/example/contents/x", "fixture-secret")
        self.assertEqual(call.call_count, 1)
        sleep.assert_not_called()

    def test_404_option_stays_read_only(self):
        err = http_error(404, "Not Found")
        with patch("sync.urlopen", side_effect=err) as call:
            self.assertIsNone(GitHubAPI().get("/repos/hibi89/example/contents/x", "fixture-secret", allow_404=True))
        self.assertEqual(call.call_count, 1)


if __name__ == "__main__":
    unittest.main()
