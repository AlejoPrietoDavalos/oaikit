from typing import Any, Optional
from abc import ABC, abstractmethod

from pydantic import BaseModel
import openai

__all__ = ["OAISchema", "FnCallOAI"]

class OAISchema(BaseModel):
    @classmethod
    def fn_tool(cls, *, name: Optional[str] = None, description: Optional[str] = None) -> dict:
        """ Retorna la tool en el formato que OpenAI espera."""
        tool = openai.pydantic_function_tool(cls, name=name, description=description)
        return tool


# TODO: Quizás crear distintas categorías o tipos de tools, clasificadores, checkeadores,...
class FnCallOAI(OAISchema, ABC):
    @classmethod
    @abstractmethod
    def fn_name(cls) -> str:
        ...
    
    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        ...
