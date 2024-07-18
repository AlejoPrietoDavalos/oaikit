from typing import List, Type, TypeVar

from pydantic import BaseModel

from oaikit.role import OAIRole, SYSTEM, USER, ASSISTANT
from oaikit.content.text import ContentText
from oaikit.content.image import ContentImage, ImageURL

__all__ = ["OAIMsg"]

T_OAIMsg = TypeVar("T_OAIMsg", bound="OAIMsg")
T_Content = str | List[ContentText | ContentImage]

class OAIMsg(BaseModel):
    role: OAIRole
    content: T_Content
    #name: str ?

    @property
    def is_system(self) -> bool:
        return self.role == SYSTEM
    
    @property
    def is_user(self) -> bool:
        return self.role == USER
    
    @property
    def is_assistant(self) -> bool:
        return self.role == ASSISTANT

    @classmethod
    def system(cls: Type[T_OAIMsg], *, content: T_Content) -> Type[T_OAIMsg]:
        return cls(role=SYSTEM, content=content)
    
    @classmethod
    def user(cls: Type[T_OAIMsg], *, content: T_Content) -> Type[T_OAIMsg]:
        return cls(role=USER, content=content)

    @classmethod
    def assistant(cls: Type[T_OAIMsg], *, content: T_Content) -> Type[T_OAIMsg]:
        return cls(role=ASSISTANT, content=content)
