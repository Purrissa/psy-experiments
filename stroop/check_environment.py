"""
check_environment.py

Проверка окружения перед запуском эксперимента.
"""

from pathlib import Path
import sys


def check_python_version():
    """
    Проверка версии Python.
    """

    version = sys.version_info

    if version < (3, 11):
        raise RuntimeError(
            "Требуется Python 3.11 или выше"
        )


def check_data_folder():
    """
    Создание папки данных.
    """

    folder = Path("data")

    folder.mkdir(
        exist_ok=True
    )


def check_psychopy():

    try:
        import psychopy

    except ImportError:

        raise RuntimeError(
            "PsychoPy не установлен"
        )


def run_checks():

    check_python_version()
    check_data_folder()
    check_psychopy()

    print(
        "Environment check passed"
    )


if __name__ == "__main__":
    run_checks()