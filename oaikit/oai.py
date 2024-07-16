from typing import Literal, List
from pathlib import Path
from abc import ABC

from openai import OpenAI, Stream
from openai.resources.chat.completions import Completions
from openai.resources.embeddings import Embeddings
from openai.resources.audio.transcriptions import Transcriptions

from oaikit.utils import iter_blocks

#from oaikit.utils import answer_from_stream
#DEFAULT_OPENAI_API_BASE = "https://api.openai.com/v1"
#openai.api_base = os.getenv(OPENAI_API_BASE, DEFAULT_OPENAI_API_BASE)

MODEL_EMBEDDING = "text-embedding-ada-002"
DEFAULT_MODEL = "gpt-4o"
LANGUAGE_DEFAULT = "es"

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
    
    def transcript(
            self,
            *,
            path_file: Path,
            language: Literal["es", "en"] = LANGUAGE_DEFAULT,
            model: str = "whisper-1"
        ) -> str:
        transcription = self.transcriptions.create(
            model = model,
            file = open(path_file, "rb"),
            language = language
        )
        return transcription.text

    def get_vectors(self, *, inputs: List[str], model = MODEL_EMBEDDING, len_blocks = 100) -> List[List[float]]:
        """ Retorna los vectores de embeddings para una lista de strings."""
        assert isinstance(inputs, list) and all(isinstance(i, str) for i in inputs), "Se espera una lista de strings a convertir en vectores."
        vectors = []
        for block in iter_blocks(inputs, len_blocks=len_blocks):
            embeddings = self.embeddings.create(input=block, model=model).data
            vectors.extend([e.embedding for e in embeddings])
        return vectors

    # def get_stream(self, *, messages: List[Dict[str, str]], model: str) -> Stream:
    #     return self.completions.create(model=model, messages=messages, stream=True)

    # def answer_from_messages(self, *, messages: List[Dict[str, str]], model: str = DEFAULT_MODEL) -> str:
    #     stream = self.get_stream(messages=messages, model=model)
    #     answer = answer_from_stream(stream=stream)
    #     return answer


class OAI(BaseOAI):
    def __init__(self, *, api_key: str):
        super().__init__(api_key=api_key)
