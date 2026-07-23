"""
stimuli.py

Генерация стимулов теста Струпа.

Автор: Варвара Решетникова
"""

from __future__ import annotations

import random
from typing import List

from .constants import (
    Stimulus,
    COLOR_NAMES,
    COLOR_TO_KEY,
)


class StimulusGenerator:
    """
    Генерирует все возможные стимулы теста Струпа.

    Каждый цикл содержит:

        4 конгруэнтных
        12 неконгруэнтных

    После завершения цикла стимулы снова
    случайным образом перемешиваются.
    """

    def __init__(self):

        self._cycle = []
        self._cycle_number = 0

        self._generate_cycle()

    # ----------------------------------------------------

    @property
    def cycle_number(self) -> int:
        return self._cycle_number

    # ----------------------------------------------------

    def _generate_cycle(self) -> None:
        """
        Создать новый цикл стимулов.
        """

        self._cycle_number += 1

        stimuli = []

        colors = list(COLOR_NAMES.keys())

        for word_color in colors:

            word = COLOR_NAMES[word_color]

            for ink_color in colors:

                congruent = word_color == ink_color

                stimuli.append(
                    Stimulus(
                        word=word,
                        ink_color=ink_color,
                        congruent=congruent,
                        correct_key=COLOR_TO_KEY[ink_color],
                    )
                )

        random.shuffle(stimuli)

        self._cycle = stimuli

    # ----------------------------------------------------

    def next_stimulus(self) -> Stimulus:
        """
        Вернуть следующий стимул.
        """

        if len(self._cycle) == 0:
            self._generate_cycle()

        return self._cycle.pop()