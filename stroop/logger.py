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
                "congruent",
                "correct_key",
                "response",
                "correct",
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
        correct: bool,
        rt_ms: int,
        timeout: bool,
        remaining_time: str,
    ):
        """
        Записать одну пробу.
        """

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

                "congruent":
                    congruent,

                "correct_key":
                    correct_key,

                "response":
                    response,

                "correct":
                    correct,

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