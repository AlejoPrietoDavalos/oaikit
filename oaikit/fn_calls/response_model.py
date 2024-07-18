from typing import Any
from abc import ABC, abstractmethod

from pydantic import BaseModel

__all__ = ["ResponseModel"]

class ResponseModel(BaseModel, ABC):
    @classmethod
    @abstractmethod
    def fn_name(cls) -> str:
        ...
    
    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        ...
