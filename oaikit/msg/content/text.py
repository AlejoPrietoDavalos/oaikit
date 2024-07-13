from typing import Literal

from pydantic import BaseModel

class ContentText(BaseModel):
    type: Literal["text"]
    text: str
