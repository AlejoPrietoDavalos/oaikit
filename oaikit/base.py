""" Abstracciones para incorporar `oaikit` dentro de un sistema con estructura de mensajes."""
from abc import ABC, abstractmethod

class MsgsOAI(ABC):
    def convert(self):
        pass
