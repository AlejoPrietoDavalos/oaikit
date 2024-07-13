from typing import Literal

from pydantic import BaseModel

__all__ = ["ImageURL", "ContentImage"]

class ImageURL(BaseModel):
    """ https://platform.openai.com/docs/guides/vision/low-or-high-fidelity-image-understanding."""
    url: str
    detail: Literal["auto", "low", "high"] = "auto"


class ContentImage(BaseModel):
    type: Literal["image_url"]
    image_url: ImageURL
