from stroop.timers import ExperimentTimer


def test_timer_format():

    timer = ExperimentTimer(120)

    timer.start()

    result = timer.formatted_remaining()

    assert len(result) == 9
    assert result[2] == ":"
    assert result[5] == "."