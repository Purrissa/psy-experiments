"""
parameters.py

Сохранение параметров запуска эксперимента.
"""

import json
from pathlib import Path

from .config import (
    EXPERIMENT_NAME,
    EXPERIMENT_VERSION,
    EXPERIMENT_DURATION,
    TRIAL_TIMEOUT,
    FULLSCREEN,
    WINDOW_SIZE,
    DATA_FOLDER,
)


def save_parameters(
    participant,
    trials: int,
):
    """
    Сохраняет параметры текущего запуска.
    """


    DATA_FOLDER.mkdir(
        exist_ok=True
    )


    filename = (
        f"{participant.participant_id}"
        "_parameters.json"
    )


    filepath = (
        DATA_FOLDER /
        filename
    )


    parameters = {

        "experiment_name":
            EXPERIMENT_NAME,

        "experiment_version":
            EXPERIMENT_VERSION,


        "participant_id":
            participant.participant_id,


        "age":
            participant.age,


        "gender":
            participant.gender,


        "date":
            participant.date,


        "duration_seconds":
            EXPERIMENT_DURATION,


        "trial_timeout_seconds":
            TRIAL_TIMEOUT,


        "number_of_trials":
            trials,


        "fullscreen":
            FULLSCREEN,


        "window_size":
            WINDOW_SIZE,
    }


    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            parameters,
            file,
            ensure_ascii=False,
            indent=4,
        )