from typing import Literal

__all__ = ["OAIModels", "T_OAIModels", "GPT_4O", "GPT_4O_MINI", "GPT_4O_2024_08_06", "GPT_4O_MINI_2024_07_18"]

GPT_4O = "gpt-4o"
GPT_4O_MINI = "gpt-4o-mini"
GPT_4O_2024_08_06 = "gpt-4o-2024-08-06"
GPT_4O_MINI_2024_07_18 = "gpt-4o-mini-2024-07-18"
T_OAIModels = Literal["gpt-4o-2024-08-06", "gpt-4o", "gpt-4o-mini", "gpt-4o-mini-2024-07-18"]

class OAIModels:
    GPT_4o = GPT_4O
    GPT_4o_mini = GPT_4O_MINI
    GPT_4o_2024_08_06 = GPT_4O_2024_08_06
    GPT_4o_mini_2024_07_18 = GPT_4O_MINI_2024_07_18
