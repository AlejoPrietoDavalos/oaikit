from typing import Literal, Type, TypeVar
from pathlib import Path
import base64

from pydantic import BaseModel

__all__ = ["ImageURL", "ContentImage"]

IMAGE_PNG = "image/png"     # Literal?
DEFAULT_DETAIL = "auto"
DetailImageURL = Literal["auto", "low", "high"]


def encode_img(path_img: Path) -> str:
    with open(path_img, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode("utf-8")
    return img_b64


class ImageURL(BaseModel):
    """ https://platform.openai.com/docs/guides/vision/low-or-high-fidelity-image-understanding."""
    url: str
    detail: DetailImageURL = DEFAULT_DETAIL


T_ContentImage = TypeVar("T_ContentImage", bound="ContentImage")
class ContentImage(BaseModel):
    image_url: ImageURL
    type: Literal["image_url"] = "image_url"

    @classmethod
    def from_path(cls: Type[T_ContentImage], *, path_img: Path, detail: DetailImageURL = DEFAULT_DETAIL) -> Type[T_ContentImage]:
        """ Abre y codifica la imagen a base64.
        - FIXME: Creo que el image/png, es el content-type o algo similar.
        """
        img_b64 = encode_img(path_img=path_img)
        return cls.from_b64(img_b64=img_b64, detail=detail)
    
    @classmethod
    def from_b64(cls: Type[T_ContentImage], *, img_b64: str, detail: DetailImageURL = DEFAULT_DETAIL) -> Type[T_ContentImage]:
        url = f"data:{IMAGE_PNG};base64,{img_b64}"
        return cls.from_url(url=url, detail=detail)

    @classmethod
    def from_url(cls: Type[T_ContentImage], *, url: str, detail: DetailImageURL = DEFAULT_DETAIL) -> Type[T_ContentImage]:
        return cls(image_url=ImageURL(url=url, detail=detail))
