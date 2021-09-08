"""
For each file named training.log in recursive subdirectories, find the last line containing 'Better eval results!'.
Print the file name, and the file lines between 3 lines above and 1 line bellow the line containing 'Better eval results!'.
"""

from pathlib import Path
from os import system

for path in Path('.').rglob('training.log'):
    print(path)
    with open(path) as file:
        lines = file.readlines()
    last_match_line = None
    for i, line in enumerate(lines):
        if "Better eval results!" in line:
            last_match_line = i
    for log_line in lines[max(0, last_match_line-3) : min(last_match_line+2, len(lines))]:
        print(' | ', log_line.rstrip('\n'))

