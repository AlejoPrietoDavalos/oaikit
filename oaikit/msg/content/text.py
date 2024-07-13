from typing import Literal

from pydantic import BaseModel

class ContentText(BaseModel):
    text: str
    type: Literal["text"] = "text"
