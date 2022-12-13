
from dataclasses import dataclass
from typing import Tuple, List

import numpy as np

from helper import load_input


UDLR = {'U': 1j, 'D': -1j, 'L': -1, 'R': 1}


def create_input():
    return load_input(9).read().splitlines()


def in_proximity(diff: complex) -> bool:
    '''
    given the complex difference between two coordinates,
    returns bool if coordinates are adjacent or not
    '''
    return True if (abs(diff.real) <= 1 and abs(diff.imag) <= 1) else False


def complex_sign(complex_number: complex) -> complex:
    '''
    given  a complex number, 
    removes magnitude from both real and imaginary parts
    '''
    i, j = complex_number.real, complex_number.imag
    return np.sign(i) + np.sign(j) * 1j


def finish_moving_tail(direction: str, tail: complex, head: complex):

    i_tail, j_tail = int(tail.real), int(tail.imag)
    i_head, j_head = int(head.real), int(head.imag)

    if direction == 'U':
        return [i_tail + j * 1j for j in range(j_tail + 1, j_head)]

    if direction == 'D':
        return [i_tail + j * 1j for j in reversed(range(j_head + 1, j_tail))]

    if direction == 'L':
        return [i + j_tail * 1j for i in reversed(range(i_head + 1, i_tail))]

    if direction == 'R':
        return [i + j_tail * 1j for i in range(i_tail + 1, i_head)]


def process_movement(movements: List[str], head=0, tail=0) -> List[complex]:
    visited = [0]

    for movement in movements:

        direction, distance = movement.split()
        head += UDLR[direction] * int(distance)
        diff = head - tail

        if in_proximity(diff):
            continue  # stop

        # check if tail needs to move diagonally
        if diff.real != 0 and diff.imag != 0:
            tail += complex_sign(diff)
            visited.append(tail)
        
        if in_proximity(diff):
            continue  # stop

        visited.extend(finish_moving_tail(direction, tail, head))
        tail = visited[-1]
    
    return visited


def process_movements(movements: List[str], head=0, tail=0) -> List[complex]:
    visited = [0]

    for movement in movements:

        direction, distance = movement.split()
        head += UDLR[direction] * int(distance)
        diff = head - tail

        if in_proximity(diff):
            continue  # stop

        # check if tail needs to move diagonally
        if diff.real != 0 and diff.imag != 0:
            tail += complex_sign(diff)
            visited.append(tail)
        
        if in_proximity(diff):
            continue  # stop

        visited.extend(finish_moving_tail(direction, tail, head))
        tail = visited[-1]
    
    return visited


def count_distinct(visited: List[complex]) -> int:
    return len(set(visited))




if __name__ == '__main__':

    movements = create_input()

    visited = process_movements(movements)

    print(count_distinct(visited))