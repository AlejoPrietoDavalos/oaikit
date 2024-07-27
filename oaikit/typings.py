from typing import TypeVar

from pydantic import BaseModel

T_BaseModel = TypeVar("T_BaseModel", bound="BaseModel")