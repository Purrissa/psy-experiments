"""
participant.py

Сбор информации об участнике.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from psychopy import gui


@dataclass
class Participant:
    """
    Информация об участнике.
    """

    participant_id: str
    age: str
    gender: str
    date: str
    mode: str = "Основной"


def collect_participant_info() -> Participant:
    """
    Показывает диалоговое окно
    и возвращает данные участника.
    """

    info = {
        "ID участника": "",
        "Возраст": "",
        "Пол": ["Ж", "М", "Другое"],
        "Режим теста": [
            "Основной",
            "Конгруэнтный",
        ],
    }

    dialog = gui.DlgFromDict(
        dictionary=info,
        title="Информация об участнике"
    )


    if not dialog.OK:
        raise SystemExit(
            "Эксперимент отменен пользователем"
        )


    participant = Participant(
        participant_id=info["ID участника"],
        age=info["Возраст"],
        gender=info["Пол"],
        mode=info["Режим теста"],
        date=datetime.now().isoformat()
    )

    return participant