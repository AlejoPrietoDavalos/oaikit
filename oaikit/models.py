from enum import Enum

__all__ = ["OAIModels"]

class OAIModels(Enum):
    """ `OAIModels.GPT_4o`"""
    GPT_4o = "gpt-4o"
    GPT_4 = "gpt-4"
    GPT_3_5_TURBO = "gpt-3.5-turbo"

    def __str__(self):
        return self.value
