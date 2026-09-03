#!/usr/bin/env python3

import PyInstaller
import subprocess


def build():

    subprocess.run([

        "pyinstaller",

        "--name",
        "AutoDiagPro",

        "--onefile",

        "src/autodiag/main.py"

    ])


if __name__ == "__main__":

    build()
