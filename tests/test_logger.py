from pathlib import Path

from stroop.logger import ExperimentLogger
from stroop.participant import Participant


def test_logger_creates_file(tmp_path):

    participant = Participant(
        participant_id="TEST",
        age="20",
        gender="X",
        date="2026"
    )


    logger = ExperimentLogger(
        participant,
        tmp_path
    )


    logger.log_trial(
        trial=1,
        word="КРАСНЫЙ",
        ink_color="red",
        congruent=True,
        correct_key="1",
        response="1",
        correct=True,
        rt_ms=500,
        timeout=False,
        remaining_time="01:59.000"
    )


    logger.close()


    files = list(
        Path(tmp_path).glob("*.csv")
    )


    assert len(files) == 1