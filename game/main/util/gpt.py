import json
import urllib.request

from game.main.model import ChatChunk

__GPT_ENTRY = "https://api.openai.com/v1/chat/completions"


def call_gpt(content: list[ChatChunk]):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {API_KEY}"
    }
    data = json.dumps(content).encode("utf-8")
    req = urllib.request.Request(__GPT_ENTRY, data, headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))
