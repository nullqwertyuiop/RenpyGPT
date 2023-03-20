from typing import TypedDict, Literal


class ChatChunk(TypedDict):
    role: Literal["system", "user", "assistant"]
    content: str


class GPTResponseChoice(TypedDict):
    index: int
    message: ChatChunk
    finish_reason: str


class GPTResponseUsage(TypedDict):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class GPTResponse(TypedDict):
    id: str
    object: str
    created: int
    choices: list[GPTResponseChoice]
    usage: GPTResponseUsage
