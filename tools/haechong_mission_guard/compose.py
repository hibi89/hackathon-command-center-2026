"""Compose governance addenda *below* the two immutable mission headers.

Pure helper: no filesystem, GitHub, secrets, or mutation side effects.
Callers must separately perform SHA-checked writes and readback.
"""
from check import MARKER, NEXT, MissionLockError

HEADER = MARKER + "\n" + NEXT + "\n"


def insert_after_mission_lock(source: str, addendum: str) -> str:
    """Insert a note without replacing/promoting the owner's primary mission."""
    if not isinstance(source, str) or not source.startswith(HEADER):
        raise MissionLockError("Cannot add governance note: active mission header is not intact")
    if not isinstance(addendum, str) or not addendum.strip():
        raise ValueError("Nonempty addendum required")
    note = addendum.strip("\n") + "\n"
    if len(note) > 16000 or MARKER in note or NEXT in note:
        raise ValueError("Oversized or unsafe mission addendum")
    if note in source:
        return source  # avoid duplicate no-op commits
    candidate = HEADER + note + source[len(HEADER):]
    assert candidate.startswith(HEADER)
    return candidate
