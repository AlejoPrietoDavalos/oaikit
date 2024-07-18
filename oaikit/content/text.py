from typing import Literal

from pydantic import BaseModel

__all__ = ["ContentText"]

class ContentText(BaseModel):
    text: str
    type: Literal["text"] = "text"
