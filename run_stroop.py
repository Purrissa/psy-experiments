from stroop.participant import collect_participant_info
from stroop.experiment import StroopExperiment
from stroop.congruent_experiment import CongruentStroopExperiment


def main():

    participant = collect_participant_info()

    if participant.mode == "Конгруэнтный":
        experiment = CongruentStroopExperiment(participant)
    else:
        experiment = StroopExperiment(participant)

    experiment.run()


if __name__ == "__main__":
    main()