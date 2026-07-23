"""
main.py

Запуск эксперимента Струпа.
"""

from .participant import collect_participant_info
from .experiment import StroopExperiment
from .congruent_experiment import CongruentStroopExperiment


def main():

    # сбор данных участника

    participant = collect_participant_info()


    print(
        """
Выберите эксперимент:

1 — Полный тест Струпа (2 минуты)
2 — Только конгруэнтные стимулы (1 минута)

"""
    )


    choice = input(
        "Введите номер режима: "
    )


    if choice == "2":

        experiment = CongruentStroopExperiment(
            participant=participant,
            duration=60
        )

    else:

        experiment = StroopExperiment(
            participant=participant,
            duration=120
        )


    experiment.run()



if __name__ == "__main__":

    main()