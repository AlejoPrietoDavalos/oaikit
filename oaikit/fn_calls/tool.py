from typing import Literal, List, TypeVar, Type

from pydantic import BaseModel, Field

from oaikit.fn_calls.response_model import ResponseModel

__all__ = ["Tool"]

TYPE_FUNCTION = "function"
T_Function = Literal["function"]

TYPE_OBJECT = "object"
T_Object = Literal["object"]


class FuncParams(BaseModel):
    type: T_Object = TYPE_OBJECT
    properties: dict
    required: List[str] = Field(default_factory=list)


class FuncCall(BaseModel):
    name: str
    description: str
    parameters: FuncParams


T_Tool = TypeVar("T_Tool", bound="Tool")

class Tool(BaseModel):
    type: T_Function = TYPE_FUNCTION
    function: FuncCall

    @classmethod
    def from_response_model(cls: Type[T_Tool], *, description: str, response_model: Type[ResponseModel]) -> Type[T_Tool]:
        return cls(
            function = FuncCall(
                name = response_model.fn_name(),
                description = description,
                parameters = FuncParams(**response_model.model_json_schema()).model_dump()
            )
        )
