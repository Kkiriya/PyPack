# Author: Émile
# Date: 2026-03-02

# --- Imports --- #
from PyPack.files import readf, absPath
from pathlib import Path

# --- translate the requirements.txt to appriopriate formating for .toml --- #
def requirements_to_dependence(file:Path):
    """Takes the requirements.txt file and prints a string with the proper formatting for pyproject.toml dependencies

    Args:
        file (str): requirements.txt
    """
    f_txt = readf(file)

    if f_txt:
        for line in f_txt:
            print(line.replace('==','>='))

path = absPath("requirements.txt")

requirements_to_dependence(path)
