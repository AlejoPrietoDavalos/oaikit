from typing import Literal, List, Dict, Any

from pydantic import BaseModel

from oaikit.func_calls.properties import PropsBase

TYPE_FUNCTION = "function"
T_Function = Literal["function"]

TYPE_OBJECT = "object"
T_Object = Literal["object"]


class FuncParams(BaseModel):
    type: T_Object = TYPE_OBJECT
    properties: Any             # TODO: Referenciar a las properties.
    required: List[str]


class FuncCall(BaseModel):
    name: str
    description: str
    parameters: FuncParams


class Tool(BaseModel):
    type: T_Function = TYPE_FUNCTION
    function: FuncCall

def tool_from_properties(*, description: str, properties: PropsBase) -> Tool:   # TODO: Referenciar a las properties.
    """ Por ahora, hago esta utilidad para generar una tool nueva rápidamente, luego hay que mejorar el circuito."""
    required = list(properties.model_dump().keys())
    parameters = FuncParams(properties=properties, required=required) # TODO: Será siempre deseable el required?
    fn_call = FuncCall(name=properties.fn_name(), description=description, parameters=parameters)
    tool = Tool(function=fn_call)
    return tool
