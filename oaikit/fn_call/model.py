from typing import Any
from abc import ABC, abstractmethod

from instructor import OpenAISchema
from instructor.utils import classproperty

__all__ = ["FnCallOAI"]


class OAISchema(OpenAISchema):
    @classproperty
    def tool(cls) -> dict:
        """ Retorna la tool en el formato que OpenAI espera."""
        return {"type": "function", "function": cls.openai_schema}


# TODO: Quizás crear distintas categorías o tipos de tools, clasificadores, checkeadores,...
class FnCallOAI(OAISchema, ABC):
    @classmethod
    @abstractmethod
    def fn_name(cls) -> str:
        ...
    
    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        ...
