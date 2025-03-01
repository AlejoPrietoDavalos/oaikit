from typing import List
from abc import ABC, abstractmethod

from pydantic import BaseModel

from oaikit.msg import OAIMsg


class BaseConvOAI(BaseModel, ABC):
    msgs: List[OAIMsg]


