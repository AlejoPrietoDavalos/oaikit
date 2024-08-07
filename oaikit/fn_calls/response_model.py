from typing import Any
from abc import ABC, abstractmethod

from instructor import OpenAISchema

__all__ = ["ResponseModelOAI"]


class OAISchema(OpenAISchema):
    @property
    def tool(self) -> dict:
        """ Retorna la tool en el formato que OpenAI espera."""
        return {"type": "function", "function": self.openai_schema}

class ResponseModelOAI(OAISchema, ABC):
    @classmethod
    @abstractmethod
    def fn_name(cls) -> str:
        ...
    
    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        ...
