from typing import Literal, Type, TypeVar
from pathlib import Path
import base64

from pydantic import BaseModel

__all__ = ["ImageURL", "ContentImage"]

IMAGE_PNG = "image/png"
DetailImageURL = Literal["auto", "low", "high"]
DEFAULT_DETAIL = "auto"

T_ContentImage = TypeVar("T_ContentImage", bound="ContentImage")


def encode_image(path_img: Path) -> str:
    with open(path_img, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode("utf-8")
    return img_b64


class ImageURL(BaseModel):
    """ https://platform.openai.com/docs/guides/vision/low-or-high-fidelity-image-understanding."""
    url: str
    detail: DetailImageURL = DEFAULT_DETAIL


class ContentImage(BaseModel):
    image_url: ImageURL
    type: Literal["image_url"] = "image_url"

    @classmethod
    def from_path(
            cls: Type[T_ContentImage],
            *,
            path_img: Path,
            detail: DetailImageURL = DEFAULT_DETAIL
        ) -> Type[T_ContentImage]:
        """ Abre y codifica la imagen a base64.
        - FIXME: Creo que el image/png, es el content-type o algo similar.
        """
        url = f"data:{IMAGE_PNG};base64,{encode_image(path_img=path_img)}"
        return cls.from_url(url=url, detail=detail)
    
    @classmethod
    def from_url(
        cls: Type[T_ContentImage],
        *,
        url: str,
        detail: DetailImageURL = DEFAULT_DETAIL
    ) -> Type[T_ContentImage]:
        return cls(image_url=ImageURL(url=url, detail=detail))