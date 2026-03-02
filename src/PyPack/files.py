# Author: Émile
# Date: 2026-03-02

# --- Imports --- #
from pathlib import Path
from PyPack.ui import printErr

# --- Stateless Functions --- #
def currentDir() -> Path:
    """Returns the current working directory

    Returns:
        Path: current working directory
    """
    return Path.cwd()

def absPath(path_to_file) -> Path:
    """returns the absolute path of the given file

    Returns:
        Path: absolute path to file
    """
    path = Path(path_to_file)
    return path.absolute()

def dirExist(path_to_file):
    return absPath(path_to_file).is_dir()

def fileExist(path_to_file):
    return absPath(path_to_file).is_file()

def readf(path_to_file):
    """Takes a file and returns a list containing each line of the file

    Args:
        file (path/to/file): file to be read
    """
    path = absPath(path_to_file)

    if not fileExist(path):
        printErr("File doesnt exist or is not here!")
        return None

    lines = []
    with open(path) as f:
        for line in f:
            lines.append(line.strip())

    return lines

# --- Testing the functions --- #
def main():
    print(currentDir())
    print(absPath("requirements.txt"))
    print(dirExist("requirements.txt"))
    print(fileExist("requirements.txt"))
    print(readf("requirements.txt"))

if __name__ == "__main__":
    main()
