from typing import Generator

from openai import Stream
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk

CONTENT = "content"

T_IterItemsStream = Generator[ChatCompletionChunk, None, None]


def iter_answer_partial(stream: Stream) -> Generator[str, None, None]:
    iter_items: T_IterItemsStream = (item for item in stream)
    for item in iter_items:
        if hasattr(item.choices[0].delta, CONTENT):
            answer_partial = item.choices[0].delta.content
            if not answer_partial:
                continue
            yield answer_partial

def answer_from_stream(stream: Stream) -> str:
    answer = ""
    for answer_partial in iter_answer_partial(stream=stream):
        answer += answer_partial
    return answer
