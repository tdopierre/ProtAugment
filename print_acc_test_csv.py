"""
For each file named training.log in recursive subdirectories, find the last line containing 'Better eval results!'.
Print the file name, and the number after 'acc:' in the next line.
"""

from collections import defaultdict
from pathlib import Path
from os import system
import argparse


sep = ','


parser = argparse.ArgumentParser()
parser.add_argument("parent_dir", help="The directory to crawl from", type=str)
args = parser.parse_args()


accuracies = defaultdict(str)

datasets = set()
regimes = set()
CKs = set()
runs = set()
seeds = set()
methods = set()

print('crawling from', Path(args.parent_dir).absolute(), '...')
for path in Path(args.parent_dir).rglob('training.log'):
    params = str(path).split('/training.log')[0].split('/')[-6:]
    regime, dataset, run, CK, seed, method = params
    run = int(run)
    seed = int(seed.lstrip('seed'))
    datasets.add(dataset)
    regimes.add(regime)
    CKs.add(CK)
    runs.add(run)
    seeds.add(seed)
    methods.add(method)
    with open(path) as file:
        lines = file.readlines()
    last_match_line = None
    for i, line in enumerate(lines):
        if "Better eval results!" in line:
            last_match_line = i
    if last_match_line is not None and len(lines) > last_match_line + 1 and 'acc:' in lines[last_match_line+1]:
        acc = lines[last_match_line+1].split('acc:')[-1].split()[0]
        print(acc, path)
        accuracies[(regime, dataset, run, CK, seed, method)] = acc

datasets = sorted(list(datasets))
regimes = sorted(list(regimes))
CKs = sorted(list(CKs))
runs = sorted(list(runs))
seeds = sorted(list(seeds))
methods = sorted(list(methods))

for method in methods:
    print("\n===", method, "===")
    for dataset in sorted(list(datasets)):
        print('\n' + dataset)
        print('', *[(regime if i==0 else '') for regime in regimes for i in range(len(CKs))], sep=sep)
        print('runs \\', *(CKs * len(regimes)), sep=sep)
        for run in runs:
            print(run, end='')
            for regime in sorted(list(regimes)):
                for CK in sorted(list(CKs)):
                    print(sep + accuracies[(regime, dataset, run, CK, seed, method)], end='')
            print()
