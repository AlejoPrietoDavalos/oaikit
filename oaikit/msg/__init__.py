from typing import List

from pydantic import BaseModel

from oaikit.msg.role import OpenAIRole
from oaikit.msg.content.text import ContentText
from oaikit.msg.content.image import ContentImage, ImageURL

ContentStr = str

__all__ = ["OAIMsg", "ContentStr", "ContentText", "ContentImage", "ImageURL", "OpenAIRole"]

class OAIMsg(BaseModel):
    role: OpenAIRole
    content: ContentStr | List[ContentStr | ContentText | ContentImage]
    #name: str ?
