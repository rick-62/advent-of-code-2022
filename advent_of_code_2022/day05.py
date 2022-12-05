from helper import load_input

from typing import Iterable


def create_input():
    return load_input(5).read().split('\n\n')
    

def initialise_stacks(raw_stacks: str) -> Dict[List[str]]:
    '''Convert raw text stacks to dictionary'''
    # Load in the stacks (naive way will do here)
    # each crate is fixed width (number of spaces)
    # Use dictionary for each stack number Dict[List[str]]
    # will need to get rerun if to reuse stacks (could use cache?)
    pass


def yield_procedure(raw_procedure: str) -> Iterable[int]:
    # loop through raw_procedures to extract values
    pass


def rearrange_crates(stacks: Dict[List[str]]):
    # for procedure in yield_procedure
    # update stacks
    pass


def extract_top_crates(stack):
    pass


if __name__ == '__main__':
    raw_stacks, raw_procedure = create_input()
    stacks = initialise_stacks(raw_stacks)
    rearrange_crates(stacks)
    print(extract_top_crates(stacks))
