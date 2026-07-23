from stroop.stimuli import StimulusGenerator


def test_generator_returns_stimulus():

    generator = StimulusGenerator(
        total_trials=10
    )

    stimulus = generator.next()

    assert stimulus.word in [
        "КРАСНЫЙ",
        "ЗЕЛЕНЫЙ",
        "СИНИЙ",
        "БЕЛЫЙ",
    ]


def test_correct_key_exists():

    generator = StimulusGenerator(
        total_trials=10
    )

    stimulus = generator.next()

    assert stimulus.correct_key in [
        "1",
        "2",
        "3",
        "4",
    ]


def test_generator_has_trials():

    generator = StimulusGenerator(
        total_trials=20
    )

    assert len(generator.trials) == 20