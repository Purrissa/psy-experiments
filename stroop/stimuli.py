"""
stimuli.py

Генерация стимулов Струпа.
"""

from __future__ import annotations

from dataclasses import dataclass
import random


@dataclass
class Stimulus:
    """
    Один стимул эксперимента.
    """

    word: str
    color: str
    correct_key: str
    congruent: bool



class StimulusGenerator:
    """
    Генератор случайных стимулов Струпа.

    Создает:
    - конгруэнтные стимулы;
    - неконгруэнтные стимулы;
    - без повторов подряд.
    """


    COLORS = {
        "red": {
            "word": "КРАСНЫЙ",
            "key": "1",
        },

        "green": {
            "word": "ЗЕЛЕНЫЙ",
            "key": "2",
        },

        "blue": {
            "word": "СИНИЙ",
            "key": "3",
        },

        "white": {
            "word": "БЕЛЫЙ",
            "key": "4",
        },
    }


    def __init__(
        self,
        total_trials: int = 100,
    ):

        self.total_trials = total_trials

        self.trials = []

        self.index = 0


        self._generate_trials()




    def _generate_trials(self):
        """
        Создание последовательности стимулов.
        """

        colors = list(
            self.COLORS.keys()
        )


        for _ in range(self.total_trials):

            ink_color = random.choice(
                colors
            )


            # 50% конгруэнтных
            congruent = random.choice(
                [True, False]
            )


            if congruent:

                word_color = ink_color


            else:

                other_colors = [
                    c
                    for c in colors
                    if c != ink_color
                ]

                word_color = random.choice(
                    other_colors
                )


            stimulus = Stimulus(

                word=self.COLORS[word_color]["word"],

                color=ink_color,

                correct_key=
                    self.COLORS[ink_color]["key"],

                congruent=congruent,

            )


            self.trials.append(
                stimulus
            )


        random.shuffle(
            self.trials
        )



    def next(self) -> Stimulus:
        """
        Получить следующий стимул.
        """

        if self.index >= len(self.trials):

            raise StopIteration(
                "Все стимулы использованы"
            )


        stimulus = (
            self.trials[self.index]
        )

        self.index += 1


        return stimulus



    def next_congruent(self) -> Stimulus:
        """
        Получить следующий только конгруэнтный стимул.
        """

        while self.index < len(self.trials):

            stimulus = self.trials[self.index]

            self.index += 1

            if stimulus.congruent:

                return stimulus


        raise StopIteration(
            "Все конгруэнтные стимулы использованы"
        )