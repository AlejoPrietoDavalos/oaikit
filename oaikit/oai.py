from typing import List, Dict
from abc import ABC

from openai import OpenAI, Stream
from openai.resources.chat.completions import Completions
from openai.resources.embeddings import Embeddings
from openai.resources.audio.transcriptions import Transcriptions

from oaikit.utils import answer_from_stream

#DEFAULT_OPENAI_API_BASE = "https://api.openai.com/v1"
#openai.api_base = os.getenv(OPENAI_API_BASE, DEFAULT_OPENAI_API_BASE)
DEFAULT_MODEL = "gpt-4o"

class BaseOAI(ABC):
    def __init__(self, *, api_key: str):
        self._client = OpenAI(api_key=api_key)

    @property
    def client(self) -> OpenAI:
        return self._client
    
    @property
    def completions(self) -> Completions:
        return self.client.chat.completions

    @property
    def embeddings(self) -> Embeddings:
        return self.client.embeddings

    @property
    def transcriptions(self) -> Transcriptions:
        return self.client.audio.transcriptions

    def get_stream(self, *, messages: List[Dict[str, str]], model: str) -> Stream:
        return self.completions.create(model=model, messages=messages, stream=True)

    def answer_from_messages(self, *, messages: List[Dict[str, str]], model: str = DEFAULT_MODEL) -> str:
        stream = self.get_stream(messages=messages, model=model)
        answer = answer_from_stream(stream=stream)
        return answer


class OAI(BaseOAI):
    def __init__(self, *, api_key: str):
        super().__init__(api_key=api_key)
