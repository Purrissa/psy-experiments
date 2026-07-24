"""
experiment.py

Основной цикл эксперимента Струпа.
"""

from __future__ import annotations

from pathlib import Path

from .config import (
    SHOW_INSTRUCTIONS,
    INSTRUCTION_TEXT,
)

from .parameters import save_parameters
from .stimuli import StimulusGenerator
from .timers import ExperimentTimer
from .keyboard import KeyboardHandler
from .logger import ExperimentLogger
from .ui import ExperimentWindow
from .participant import Participant



class StroopExperiment:
    """
    Главный класс эксперимента.
    """


    def __init__(
        self,
        participant: Participant,
        duration: float = 120,
        trials: int = 100,
    ):

        self.participant = participant

        self.duration = duration

        self.trials = trials


        self.timer = ExperimentTimer(
            duration
        )


        self.keyboard = KeyboardHandler(
            timeout=2
        )


        self.ui = ExperimentWindow()


        self.generator = StimulusGenerator(
            total_trials=trials
        )


        self.logger = ExperimentLogger(
            participant,
        )


        # сохраняем параметры запуска

        save_parameters(
            participant,
            trials
        )


    # --------------------------------------------------


    def run(self):
        """
        Запуск эксперимента.
        """


        # инструкция показывается до старта таймера

        if SHOW_INSTRUCTIONS:

            self.ui.show_instruction()


        # теперь начинается экспериментальное время

        self.timer.start()


        trial_number = 0


        while (
            not self.timer.finished()
            and trial_number < self.trials
        ):

            trial_number += 1


            self.run_trial(
                trial_number
            )


        self.finish()



    # --------------------------------------------------


    def run_trial(
        self,
        trial_number: int,
    ):
        """
        Одна проба Струпа.
        """


        stimulus = (
            self.generator.next()
        )


        # фиксационный крест

        self.ui.show_fixation()



        # предъявление стимула

        self.ui.show_stimulus(
            stimulus.word,
            stimulus.color
        )


        response = (
            self.keyboard
            .wait_for_response(
                ui=self.ui,
                experiment_timer=self.timer,
            )
        )


        correct = (
            response.key
            ==
            stimulus.correct_key
        )

        if response.timeout:

            accuracy = "TIMEOUT"

        elif correct:

            accuracy = "CORRECT"

        else:

             accuracy = "INCORRECT"


        # обратная связь

        if response.timeout:

            self.ui.show_feedback(
                "ВРЕМЯ ВЫШЛО",
                "orange",
                0.7
            )


        elif not correct:

            self.ui.show_feedback(
                "ОШИБКА",
                "red",
                0.7
            )


        else:

            self.ui.show_feedback(
                "ВЕРНО",
                "green",
                0.5
            )



        # очистка перед следующей пробой

        self.ui.clear()



        # запись данных
        
        if response.timeout:
            accuracy = "TIMEOUT"

        elif correct:
            accuracy = "CORRECT"

        else:
            accuracy = "INCORRECT"

        self.logger.log_trial(
            trial=trial_number,
            word=stimulus.word,
            ink_color=stimulus.color,
            congruent=stimulus.congruent,
            correct_key=stimulus.correct_key,
            response=response.key,
            accuracy=accuracy,
            rt_ms=response.rt_ms,
            timeout=response.timeout,
            remaining_time=self.timer.formatted_remaining(),
        )



    # --------------------------------------------------


    def finish(self):
        """
        Завершение эксперимента.
        """


        self.logger.close()


        self.ui.show_feedback(
            "Эксперимент завершен.\nСпасибо!",
            "white",
            2
        )


        self.ui.close()