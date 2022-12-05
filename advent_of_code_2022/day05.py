import re

from collections import defaultdict
from typing import Iterable, Dict, List

from helper import load_input


def create_input():
    return load_input(5).read().split('\n\n')
    

def initialise_stacks(raw_stacks: str) -> Dict[int, List[str]]:
    '''Convert raw text stacks to dictionary'''

    # intiialise stacks dict
    stacks = defaultdict(list)

    # split crates & separate stack ids
    lines = raw_stacks.splitlines()
    stack_ids = lines.pop(-1)

    # Load in the stacks (naive way will do here)   
    for stack in re.finditer(r'\d', stack_ids):
        stacks[int(stack.group())] = [
            line[stack.start()] for line in lines[::-1] if line[stack.start()] != ' '
        ]
    return stacks


def yield_procedure(raw_procedures: str) -> Iterable[int]:
    '''yield the next procedure, extracting 3 key values'''
    for procedure in raw_procedures.splitlines():
        yield [int(d) for d in re.findall(r'\d+', procedure)]


def rearrange_crates(raw_procedures, stacks: Dict[int, List[str]]):
    '''Rearrange crates moving 1 crate at a time, n times'''
    for n, i1, i2 in yield_procedure(raw_procedures):
        for _ in range(n):
            stacks[i2].append(stacks[i1].pop())
    return stacks


def rearrange_crates_9001(raw_procedures, stacks: Dict[int, List[str]]):
    '''Rearrange crates moving n crates at a time'''
    for n, i1, i2 in yield_procedure(raw_procedures):
        stacks[i2].extend(stacks[i1][-n:])
        del stacks[i1][-n:]
    return stacks


def extract_top_crates(stack):
    return ''.join(v[-1] for k,v in stack.items())


if __name__ == '__main__':

    raw_stacks, raw_procedures = create_input()

    # Part 1
    stacks = initialise_stacks(raw_stacks)
    rearrange_crates(raw_procedures, stacks)
    print(extract_top_crates(stacks))

    # Part 2
    stacks = initialise_stacks(raw_stacks)
    rearrange_crates_9001(raw_procedures, stacks)
    print(extract_top_crates(stacks))

