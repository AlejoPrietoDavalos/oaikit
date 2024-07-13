from typing import Literal, Type, TypeVar
from pathlib import Path
import base64

from pydantic import BaseModel

__all__ = ["ImageURL", "ContentImage"]

def encode_image(path_img: Path) -> str:
    with open(path_img, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode("utf-8")
    return img_b64

IMAGE_PNG = "image/png"
DetailImageURL = Literal["auto", "low", "high"]

class ImageURL(BaseModel):
    """ https://platform.openai.com/docs/guides/vision/low-or-high-fidelity-image-understanding."""
    url: str
    detail: DetailImageURL = "auto"


T_ContentImage = TypeVar("T_ContentImage", bound="ContentImage")

class ContentImage(BaseModel):
    type: Literal["image_url"] = "image_url"
    image_url: ImageURL

    @classmethod
    def from_path(
            cls: Type[T_ContentImage],
            *,
            path_img: Path,
            detail: DetailImageURL = None
        ) -> Type[T_ContentImage]:
        """ Abre y codifica la imagen a base64.
        - FIXME: Creo que el image/png, es el content-type o algo similar.
        """
        params = {"url": f"data:{IMAGE_PNG};base64,{encode_image(path_img=path_img)}"}
        if detail is not None:
            params["detail"] = detail
        image_url = ImageURL(**params)
        return cls(image_url=image_url)
