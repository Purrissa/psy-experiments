"""
timers.py

Таймеры для эксперимента Струпа.
"""

from __future__ import annotations

from psychopy import core


class ExperimentTimer:
    """
    Общий таймер эксперимента.

    Используется для обратного отсчета
    всей экспериментальной сессии.
    """

    def __init__(self, duration_seconds: float):

        self.duration = duration_seconds

        self.clock = core.Clock()

        self.started = False


    def start(self):
        """
        Запустить таймер.
        """

        self.clock.reset()

        self.started = True


    def elapsed(self) -> float:
        """
        Возвращает прошедшее время в секундах.
        """

        if not self.started:
            return 0.0

        return self.clock.getTime()


    def remaining(self) -> float:
        """
        Возвращает оставшееся время.
        """

        remaining = (
            self.duration
            - self.elapsed()
        )

        return max(
            remaining,
            0.0
        )


    def finished(self) -> bool:
        """
        Проверка окончания эксперимента.
        """

        return self.remaining() <= 0


    def formatted_remaining(self) -> str:
        """
        Формат:

        MM:SS.mmm
        """

        milliseconds = int(
            self.remaining() * 1000
        )

        minutes = milliseconds // 60000

        seconds = (
            milliseconds % 60000
        ) // 1000

        ms = milliseconds % 1000


        return (
            f"{minutes:02d}:"
            f"{seconds:02d}."
            f"{ms:03d}"
        )


# ========================================================
# Таймер отдельной пробы
# ========================================================


class TrialTimer:
    """
    Таймер реакции на отдельный стимул.
    """

    def __init__(self):

        self.clock = core.Clock()


    def start(self):
        """
        Начало измерения RT.
        """

        self.clock.reset()


    def reaction_time(self) -> float:
        """
        Время реакции в секундах.
        """

        return self.clock.getTime()


    def reaction_time_ms(self) -> int:
        """
        Время реакции в миллисекундах.
        """

        return int(
            self.clock.getTime() * 1000
        )