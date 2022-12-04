from typing import List

import re

from helper import load_input


def create_input():
    return load_input(4).read().replace('\n', ' ').split()


def full_overlap(a,b,c,d):
    '''conditional function for part 1'''
    if a >= c and b <= d: return True
    if a <= c and b >= d: return True
    return False


def partial_overlap(a,b,c,d):
    '''conditional function for part 2'''
    if b >= c and b <= d: return True
    if a >= c and a <= d: return True
    return full_overlap(a,b,c,d)


def check_section_overlap(string: str, fn=full_overlap) -> bool:
    '''Extracts four integers from string and applies conditional function'''
    return fn(*[int(num) for num in re.split('[,-]+', string)])
    

def sum_overlap(input_list: List, fn) -> int:
    '''loops through input list summing where there is overlap (True)'''
    return sum([check_section_overlap(string, fn) for string in input_list])


if __name__ == '__main__':

    # Part 1
    print(sum_overlap(create_input(), full_overlap))

    # Part 2
    print(sum_overlap(create_input(), partial_overlap))