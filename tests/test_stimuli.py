"""
Тесты генератора стимулов.
"""

from stroop.stimuli import StimulusGenerator


def test_cycle_contains_16_unique_stimuli():

    generator = StimulusGenerator()

    stimuli = [
        generator.next_stimulus()
        for _ in range(16)
    ]

    assert len(stimuli) == 16

    unique = {
        (s.word, s.ink_color)
        for s in stimuli
    }

    assert len(unique) == 16


def test_congruency_counts():

    generator = StimulusGenerator()

    stimuli = [
        generator.next_stimulus()
        for _ in range(16)
    ]

    congruent = sum(
        s.congruent
        for s in stimuli
    )

    incongruent = sum(
        not s.congruent
        for s in stimuli
    )

    assert congruent == 4
    assert incongruent == 12


def test_second_cycle_is_new():

    generator = StimulusGenerator()

    first = [
        generator.next_stimulus()
        for _ in range(16)
    ]

    second = [
        generator.next_stimulus()
        for _ in range(16)
    ]

    assert len(first) == 16
    assert len(second) == 16

    unique = {
        (s.word, s.ink_color)
        for s in second
    }

    assert len(unique) == 16