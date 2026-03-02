# PyPack

My Personal Python Package

---

## Fonctions Included:

### UI Related `ui.py`

- **Title Message: `printHead(str)`** Prints a given string with surrounding '---' or '==='
- **Colour Message: `printCol(str, col)`** Prints a given string in the given colour
  - Supported Colours:
    - Black
    - Red
    - Green
    - Yellow
    - Blue
    - Magenta
    - Cyan
    - White
    - Reset
- **Coloured Title Message: `printColHead(str, col, dash_or_equal)`** Prints a given string with surrounding '---' or '===' and in the given colour
- **Highlighted Message: `printHigh(str)`** Prints a given str with a yellow background
- **Error Message: `printErr(msg)`** Prints a given str in red
- **Success Message: `printSuc(msg)`** Prints a given str in green

- **Wait:** Pause the program for the given int in seconds

### File & Path `files.py`

- **Current Directory: `currentDir()`** Returns the current working dir
- **Absolute Path: `absPath(path_to_file)`** Returns the absolute path of the given file
- **Existing Directory: `dirExist('path')`** Returns true if the dir exist, has an option to create it if it doesnt
- **Existing File: `fileExist('file')`** Returns true if a file exist
- **Read file: `readf(path_to_file)`** Returns a list of string with every line of a given file

### Collections (List, Tuples, Sets, Dict) `colls.py`

- **Flatten Nested List:** Flattens nested lists/tuples into a single list

### Strings

- **Is Blank:** Returns true for None, empty or whitespace only string

### Numbers (int, float, hex, ...) `nums.py`

- **Convert Number:** Converts given number into desired base
