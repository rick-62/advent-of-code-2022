
import re

from collections import defaultdict
from typing import List, Dict

from helper import load_input


def create_input():
    return load_input(7).read()


def create_dir_store(terminal_output: str) -> Dict[str, int]:
    '''
    loop through terminal input:
        - store: record directory (direct) sizes as dict 
        - dirs: record all possible directories (important)
        - wd: update current working directory
    '''
    store = defaultdict(int)
    dirs = set()
    wd = []
    for line in terminal_output.splitlines():
        if line == '':
            continue
        if line.startswith('$ cd ..'):
            wd.pop()
        elif line.startswith('$ cd'):
            wd.append(line[5:])
            dirs.add('-'.join(wd))
        elif line[0].isdigit():
            store['-'.join(wd)] += (int(line.split()[0]))
    return store, dirs


def tally_each_dir(dirs: set, store: Dict[str, int]) -> Dict[str, int]:
    '''sums direct & indirect directory sizes'''
    return {
        d: sum([v for k, v in store.items() if k.startswith(d) or (d == '/')]) 
        for d in dirs
    }


def sum_dirsizes_lt_100000(dirsizes: Dict[str, int]) -> int:
    return sum([x for x in dirsizes.values() if x <= 100_000])


def calc_space_required(current):
    TOTAL = 70_000_000
    UPDATE = 30_000_000
    return UPDATE - (TOTAL - current)


def size_of_smallest_dir_to_remove(dirsizes: Dict[str, int]):
    '''
    retrieves total size of smallest possible directory,
    which can be removed to ensure sufficient space for update
    '''
    min_dir_sizes = [
        v for v in sorted(list(dirsizes.values()))
        if v >= calc_space_required(dirsizes['/'])
    ]
    return min_dir_sizes[0]  
   

if __name__ == '__main__':

    terminal_output = create_input()
    store, dirs = create_dir_store(terminal_output)
    dirsizes = tally_each_dir(dirs, store)

    # Part 1
    print(sum_dirsizes_lt_100000(dirsizes))

    # Part 2
    print(size_of_smallest_dir_to_remove(dirsizes))

