"""
ui.py

Визуальный интерфейс эксперимента PsychoPy.
"""

from __future__ import annotations

from psychopy import visual, core, event

from .config import (
    FULLSCREEN,
    WINDOW_SIZE,
    BACKGROUND_COLOR,
    FONT,
    WORD_SIZE,
    TIMER_SIZE,
    FEEDBACK_SIZE,
    WORD_POSITION,
    TIMER_POSITION,
    FIXATION_POSITION,
    TEXT_COLOR,
    TIMER_COLOR,
)



class ExperimentWindow:
    """
    Окно эксперимента PsychoPy.
    """


    def __init__(self):

        self.window = visual.Window(
            size=WINDOW_SIZE,
            fullscr=FULLSCREEN,
            color=BACKGROUND_COLOR,
            units="height",
        )


        self.word = visual.TextStim(
            self.window,
            text="",
            font=FONT,
            height=WORD_SIZE,
            pos=WORD_POSITION,
            color=TEXT_COLOR,
        )


        self.timer = visual.TextStim(
            self.window,
            text="",
            font=FONT,
            height=TIMER_SIZE,
            pos=TIMER_POSITION,
            color=TIMER_COLOR,
        )


        self.fixation = visual.TextStim(
            self.window,
            text="+",
            font=FONT,
            height=WORD_SIZE,
            pos=FIXATION_POSITION,
            color=TEXT_COLOR,
        )


        self.feedback = visual.TextStim(
            self.window,
            text="",
            font=FONT,
            height=FEEDBACK_SIZE,
            pos=(0, 0),
        )


        # состояние текущего кадра

        self.current_word = False
        self.current_timer = False



    def draw(self):
        """
        Отрисовать текущий кадр.
        """

        if self.current_word:
            self.word.draw()


        if self.current_timer:
            self.timer.draw()


        self.window.flip()



    def show_fixation(
        self,
        duration=0.5,
    ):

        self.fixation.draw()

        self.window.flip()

        core.wait(duration)



    def show_stimulus(
        self,
        word: str,
        color: str,
    ):
        """
        Установить текущий стимул.
        """

        self.word.text = word
        self.word.color = color

        self.current_word = True



    def show_timer(
        self,
        value: str,
    ):
        """
        Установить таймер.
        """

        self.timer.text = value

        self.current_timer = True



    def show_feedback(
        self,
        text: str,
        color: str,
        duration: float,
    ):
        """
        Показать сообщение.
        """

        self.feedback.text = text
        self.feedback.color = color

        self.feedback.draw()

        self.window.flip()

        core.wait(duration)



    def clear(self):
        """
        Очистить экран.
        """

        self.current_word = False
        self.current_timer = False

        self.window.flip()



    def show_instruction(
        self,
        text: str,
    ):
        """
        Экран инструкции.
        """

        lines = [

            ("Тест Струпа.", "white"),

            ("", "white"),

            ("Вам будут показаны слова,", "white"),
            ("окрашенные в разные цвета.", "white"),

            ("", "white"),

            ("Ваша задача:", "white"),
            ("нажимать клавишу,", "white"),
            ("соответствующую ЦВЕТУ текста,", "yellow"),
            ("а не значению слова.", "white"),

            ("1 — красный", "red"),
            ("2 — зеленый", "green"),
            ("3 — синий", "blue"),
            ("4 — белый", "white"),

            ("", "white"),

            ("Отвечайте как можно быстрее и точнее.", "white"),

            ("", "white"),

            ("Нажмите ПРОБЕЛ для начала.", "yellow"),
        ]


        start_y = 0.42
        step = 0.055


        for i, (line, color) in enumerate(lines):
            
            size = 0.03

            if "ЦВЕТУ" in line:
             size = 0.035


            stimulus = visual.TextStim(
                self.window,
                text=line,
                font=FONT,
                height=size,
                color=color,
                pos=(0, start_y - i * step),
                alignText="center",
            )

            stimulus.draw()


        self.window.flip()


        event.waitKeys(
            keyList=["space"]
        )