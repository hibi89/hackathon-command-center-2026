import { health, receiveWebhook } from "../lib/receiver.js";

export function GET() {
  return health(process.env);
}

export async function POST(request) {
  return receiveWebhook(request, process.env);
}
