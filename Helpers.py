import os
from os import path

import requests


def loadEnv():
    with open('.env') as f:
        return dict(x.rstrip().split("=", 1) for x in f)


def getInput(day: int):
    with open("Inputs/input_" + str(day)) as inputFile:
        return inputFile.read()


folder = "Inputs"


def download_input(year, day):
    env = loadEnv()
    if not path.exists(folder):
        os.mkdir(folder)
    filename = "input_" + str(day)
    filepath = path.join(folder, filename)
    if path.isfile(filepath):
        print("file already there")
        return
    print("fetching file")
    r = requests.get(f'https://adventofcode.com/2023/day/{day}/input', cookies={"session": env["USER_SESSION_ID"]})
    r.raise_for_status()
    with open(filepath, "w") as inputfile:
        inputfile.write(r.text)


if __name__ == "__main__":
    download_input(2023, 1)
