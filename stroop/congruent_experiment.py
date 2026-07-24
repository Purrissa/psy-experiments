from pathlib import Path

from .stimuli import StimulusGenerator
from .timers import ExperimentTimer
from .keyboard import KeyboardHandler
from .logger import ExperimentLogger
from .ui import ExperimentWindow


class CongruentStroopExperiment:


    def __init__(
        self,
        participant,
        duration=60,
        trials=999,
    ):

        self.participant = participant

        self.timer = ExperimentTimer(
            duration
        )

        self.keyboard = KeyboardHandler(
            timeout=5
        )

        self.ui = ExperimentWindow()

        self.generator = StimulusGenerator(
            total_trials=trials
        )

        self.logger = ExperimentLogger(
            participant,
        )



    def run(self):

        self.ui.show_instruction()

        self.timer.start()

        trial = 0


        while not self.timer.finished():

            trial += 1

            stimulus = (
                self.generator.next_congruent()
            )


            self.ui.show_fixation()


            self.ui.show_stimulus(
                stimulus.word,
                stimulus.color
            )


            response = (
                self.keyboard.wait_for_response(
                    ui=self.ui,
                    experiment_timer=self.timer,
                    show_timer=False,
                )
            )


            correct = (
                response.key
                ==
                stimulus.correct_key
            )


            self.logger.log_trial(
                trial=trial,
                word=stimulus.word,
                ink_color=stimulus.color,
                congruent=True,
                correct_key=stimulus.correct_key,
                response=response.key,
                correct=correct,
                rt_ms=response.rt_ms,
                timeout=response.timeout,
                remaining_time=
                    self.timer.formatted_remaining()
            )


        self.logger.close()
        self.ui.close()