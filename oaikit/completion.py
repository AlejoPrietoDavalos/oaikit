from typing import Generator, Literal, List

from openai.types.chat.chat_completion import ChatCompletion, Choice, ChatCompletionMessage
from openai.types.chat.chat_completion_message_tool_call import ChatCompletionMessageToolCall

__all__ = ["ChatCompletionHandler"]

ChoiceFinishReason = Literal["stop", "length", "tool_calls", "content_filter", "function_call"]

class ChatCompletionHandler:
    def __init__(self, response: ChatCompletion):
        self.response: ChatCompletion = response

    @property
    def choice(self) -> Choice:
        return self.response.choices[0]

    @property
    def message(self) -> ChatCompletionMessage:
        return self.choice.message

    @property
    def finish_reason(self) -> ChoiceFinishReason:
        """ Razón por la que el modelo deja de generar tokens."""
        return self.choice.finish_reason

    @property
    def tool_calls(self) -> List[ChatCompletionMessageToolCall]:
        return self.message.tool_calls

    def iter_tool_call(self) -> Generator[ChatCompletionMessageToolCall, None, None]:
        return (tool_call for tool_call in self.tool_calls)
