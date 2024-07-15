from typing import Literal, List, Any, Tuple
from abc import ABC, abstractmethod

from pydantic import BaseModel

__all__ = ["FuncPropStr", "FuncPropEnum", "PropsBase", "DataPropsBase"]

TYPE_STRING = "string"
T_String = Literal["string"]

class FuncPropStr(BaseModel):
    type: T_String = TYPE_STRING
    description: str

class FuncPropEnum(BaseModel):
    type: T_String = TYPE_STRING
    enum: List[str]     # Categorical values.
    description: str


class PropsBase(BaseModel, ABC):
    @classmethod
    @abstractmethod
    def fn_name(cls) -> str:
        """ Retorna el nombre de la function call asociada."""
        ...


class DataPropsBase(BaseModel, ABC):
    @classmethod
    @abstractmethod
    def fn_name(cls) -> str:
        """ Retorna el nombre de la function call asociada."""
        ...
    
    @abstractmethod
    def execute(self, *args, **kwargs) -> Tuple[str, Any]:
        """ Ejecuta la función y realiza acciones."""
        ...
