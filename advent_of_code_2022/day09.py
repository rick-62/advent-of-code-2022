
from collections import defaultdict
from functools import lru_cache
from typing import Tuple, List

import numpy as np

from helper import load_input


UDLR = {'U': 1j, 'D': -1j, 'L': -1, 'R': 1}


def create_input():
    return load_input(9).read().splitlines()


@lru_cache
def in_proximity(diff: complex) -> bool:
    '''
    given the complex difference between two coordinates,
    returns bool if coordinates are adjacent or not
    '''
    return True if (abs(diff.real) <= 1 and abs(diff.imag) <= 1) else False


@lru_cache
def complex_sign(complex_number: complex) -> complex:
    '''
    given  a complex number, 
    removes magnitude from both real and imaginary parts
    '''
    i, j = complex_number.real, complex_number.imag
    return np.sign(i) + np.sign(j) * 1j


@lru_cache
def finish_moving_tail(tail: complex, head: complex):

    i_tail, j_tail = int(tail.real), int(tail.imag)
    i_head, j_head = int(head.real), int(head.imag)

    if j_head > j_tail:
        return [i_tail + j * 1j for j in range(j_tail + 1, j_head)]

    if j_head < j_tail:
        return [i_tail + j * 1j for j in reversed(range(j_head + 1, j_tail))]

    if i_head < i_tail:
        return [i + j_tail * 1j for i in reversed(range(i_head + 1, i_tail))]

    if i_head > i_tail:
        return [i + j_tail * 1j for i in range(i_tail + 1, i_head)]


@lru_cache
def process_movement(head: complex = 0, tail: complex = 0) -> List[complex]:
    visited = []

    diff = head - tail

    if in_proximity(diff):
        return visited

    # check if tail needs to move diagonally
    while diff.real != 0 and diff.imag != 0:
        tail += complex_sign(diff)
        visited.append(tail)
        diff = head - tail

        if in_proximity(diff):
            return visited
    
    visited.extend(finish_moving_tail(tail, head))
    
    return visited



def process_movements(movements: List[str], n_tails: int = 9):
    visited = [0]
    knots = defaultdict(complex)

    for movement in movements:
        print(movement, knots)

        direction, distance = movement.split()
        knots[0] += UDLR[direction] * int(distance)

        for n in range(1, n_tails + 1):
            head = knots[n-1]
            tail = knots[n]
            
            _visited = process_movement(head=head, tail=tail)
            knots[n] = _visited[-1] if _visited else knots[n]

        visited.extend(_visited)

    return visited         



def count_distinct(visited: List[complex]) -> int:
    return len(set(visited))




if __name__ == '__main__':

    movements = create_input()

    visited = process_movements(movements, n_tails=1)

    print(count_distinct(visited))

    visited = process_movements(movements, n_tails=9)

    print(count_distinct(visited))