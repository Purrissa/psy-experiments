"""
constants.py

Константы для теста Струпа.
"""

from dataclasses import dataclass


# --------------------------------------------------------
# Цвета PsychoPy
# --------------------------------------------------------

RED = "red"
GREEN = "green"
BLUE = "blue"
WHITE = "white"

COLOR_NAMES = {
    RED: "КРАСНЫЙ",
    GREEN: "ЗЕЛЕНЫЙ",
    BLUE: "СИНИЙ",
    WHITE: "БЕЛЫЙ",
}


# --------------------------------------------------------
# Соответствие клавиш цветам
# --------------------------------------------------------

KEY_MAPPING = {
    "1": RED,
    "2": GREEN,
    "3": BLUE,
    "4": WHITE,
}

COLOR_TO_KEY = {
    RED: "1",
    GREEN: "2",
    BLUE: "3",
    WHITE: "4",
}


# --------------------------------------------------------
# Стимул
# --------------------------------------------------------

@dataclass(frozen=True)
class Stimulus:
    """
    Один стимул теста Струпа.
    """

    word: str
    ink_color: str
    congruent: bool
    correct_key: str