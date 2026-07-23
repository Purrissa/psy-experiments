"""
main.py

Точка запуска эксперимента Струпа.
"""

from .participant import collect_participant_info
from .experiment import StroopExperiment

from .config import (
    EXPERIMENT_DURATION,
)



def main():

    # окно ввода информации об участнике

    participant = (
        collect_participant_info()
    )


    # запуск эксперимента

    experiment = StroopExperiment(
        participant=participant,
        duration=EXPERIMENT_DURATION,
        trials=100,
    )


    experiment.run()



if __name__ == "__main__":

    main()