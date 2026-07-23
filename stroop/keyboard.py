"""
keyboard.py

Обработка ответов участника.
"""

from __future__ import annotations

from dataclasses import dataclass

from psychopy import event, core

from .config import (
    ALLOWED_KEYS,
    EXIT_KEY,
)

from .timers import TrialTimer



@dataclass
class Response:
    """
    Ответ участника.
    """

    key: str | None
    rt_ms: int
    timeout: bool



class KeyboardHandler:
    """
    Управление вводом с клавиатуры.
    """


    def __init__(
        self,
        timeout: float = 5,
    ):

        self.timeout = timeout



    def wait_for_response(
        self,
        ui=None,
        experiment_timer=None,
    ) -> Response:
        """
        Ожидание ответа участника.

        Во время ожидания:
        - обновляется экран;
        - отображается таймер;
        - отслеживается таймаут.
        """


        event.clearEvents()


        timer = TrialTimer()

        timer.start()



        while True:


            keys = event.getKeys(
                keyList=[
                    *ALLOWED_KEYS,
                    EXIT_KEY,
                ]
            )


            if keys:

                key = keys[0]


                if key == EXIT_KEY:

                    raise SystemExit(
                        "Эксперимент остановлен"
                    )


                return Response(
                    key=key,
                    rt_ms=timer.reaction_time_ms(),
                    timeout=False,
                )



            # обновляем экран

            if ui is not None:


                if experiment_timer is not None:

                    ui.show_timer(
                        experiment_timer.formatted_remaining()
                    )


                ui.draw()



            # проверяем время ответа

            if timer.reaction_time() >= self.timeout:


                return Response(
                    key=None,
                    rt_ms=timer.reaction_time_ms(),
                    timeout=True,
                )



            core.wait(
                0.01
            )