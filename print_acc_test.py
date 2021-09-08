"""
For each file named training.log in recursive subdirectories, find the last line containing 'Better eval results!'.
Print the file name, and the number after 'acc:' in the next line.
"""

from pathlib import Path
from os import system

print('accutacy logging_file')
for path in Path('.').rglob('training.log'):
    with open(path) as file:
        lines = file.readlines()
    last_match_line = None
    for i, line in enumerate(lines):
        if "Better eval results!" in line:
            last_match_line = i
    if last_match_line is not None:
        print(lines[min(last_match_line+1, len(lines))].split('acc:')[-1].split()[0], path)

