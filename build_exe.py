from PyInstaller.__main__ import run


if __name__ == "__main__":

    opts = [
        "run_stroop.py",

        "--name=StroopTest",

        "--onefile",

        "--windowed",

        "--clean",

        "--collect-all",
        "psychopy",

        "--hidden-import",
        "stroop",

        "--hidden-import",
        "stroop.experiment",

        "--hidden-import",
        "stroop.congruent_experiment",

        "--hidden-import",
        "stroop.participant",

        "--hidden-import",
        "stroop.ui",

        "--hidden-import",
        "stroop.logger",

        "--hidden-import",
        "stroop.stimuli",

        "--hidden-import",
        "stroop.keyboard",

        "--hidden-import",
        "stroop.timers",
    ]

    run(opts)