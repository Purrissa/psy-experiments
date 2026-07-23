"""
logger.py

Сохранение данных эксперимента.
"""

from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path

from .participant import Participant


class ExperimentLogger:
    """
    Логгер эксперимента.

    Создает CSV-файл и записывает
    каждую пробу отдельно.
    """

    def __init__(
        self,
        participant: Participant,
        folder: Path,
    ):

        self.participant = participant

        folder.mkdir(
            exist_ok=True
        )

        timestamp = (
            datetime.now()
            .strftime("%Y%m%d_%H%M%S")
        )

        filename = (
            f"{participant.participant_id}_"
            f"stroop_{timestamp}.csv"
        )

        self.filepath = folder / filename


        self.file = open(
            self.filepath,
            "w",
            newline="",
            encoding="utf-8"
        )


        self.writer = csv.DictWriter(
            self.file,
            fieldnames=[
                "participant_id",
                "date",
                "trial",
                "word",
                "ink_color",
                "condition",
                "congruent",
                "correct_key",
                "response",
                "accuracy",
                "rt_ms",
                "timeout",
                "remaining_time",
            ]
        )


        self.writer.writeheader()



    def log_trial(
        self,
        *,
        trial: int,
        word: str,
        ink_color: str,
        congruent: bool,
        correct_key: str,
        response: str | None,
        rt_ms: int | None,
        timeout: bool,
        remaining_time: str,
        accuracy: str | None = None,
        correct: bool | None = None,
    ):
        """
        Записать одну пробу.
        """

        if accuracy is None:

            if timeout:
                accuracy = "TIMEOUT"

            elif correct:
                accuracy = "CORRECT"

            else:
                accuracy = "INCORRECT"

        condition = (
            "CONGRUENT"
            if congruent
            else
            "INCONGRUENT"
        )


        self.writer.writerow(
            {
                "participant_id":
                    self.participant.participant_id,

                "date":
                    self.participant.date,

                "trial":
                    trial,

                "word":
                    word,

                "ink_color":
                    ink_color,

                "condition":
                    condition,

                "congruent":
                    congruent,

                "correct_key":
                    correct_key,

                "response":
                    response,

                "accuracy":
                    accuracy,

                "rt_ms":
                    rt_ms,

                "timeout":
                    timeout,

                "remaining_time":
                    remaining_time,
            }
        )


        self.file.flush()



    def close(self):
        """
        Закрыть файл.
        """

        self.file.close()