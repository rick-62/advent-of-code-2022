import string
from typing import List

from itertools import combinations

from helper import load_input


def create_input():
    return load_input(3).read().replace('\n', ' ').split()

##################
# --- Part 1 --- #
##################

def split_into_equal_chunks(string: str, n_chunks=2):
    '''split string evenly into n chunks''' 

    len_chunk = int(len(string)/n_chunks)

    return [
        string[i:i+len_chunk] 
        for i in range(0, len(string), len_chunk)
    ]


def extract_common_item(lst: List[str]) -> str:

    # convert list of strings to list of sets
    setlist = [set(string) for string in lst]

    # identify common letters between combinations of sets
    common_items = set.intersection(*setlist)

    # return distinct string of common letters
    return ''.join(common_items)


def calculate_total_score(common_items):
    return sum([string.ascii_letters.index(item) + 1 for item in common_items])


def extract_all_common_items_between_compartments(bags):
    return ''.join(
        [extract_common_item(split_into_equal_chunks(bag)) for bag in bags]
    )


##################
# --- Part 2 --- #
##################

def split_list_into_groups(lst: List[str], n_groups=3):
    return [lst[i:i+n_groups] for i in range(0, len(lst), n_groups)]



def extract_all_common_items_between_groups(bags):
    return ''.join(
        [extract_common_item(group) for group in split_list_into_groups(bags)]
    )

    




if __name__ == '__main__':
    bags = create_input()
    common_items = extract_all_common_items_between_compartments(bags)
    print(calculate_total_score(common_items))

    print(bags[:3])
    print(split_list_into_groups(bags)[0])
    print(extract_common_item(['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg']))

    common_items = extract_all_common_items_between_groups(bags)
    print(calculate_total_score(common_items))
