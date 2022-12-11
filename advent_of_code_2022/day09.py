
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
        return [i_tail + j * 1j for j in reversed(range(j_headi_head + 1, j_tail))]

    if direction == 'L':
        return [i + j_tail for i in reversed(range(i_head + 1, i_tail))]

    if direction == 'R':
        return [i + j_tail for i in range(i_tail + 1, i_head)]



def process_movements(movements: List[str]) -> List[complex]:
    visited = [0]
    head = 0
    tail = 0

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



        


        
    return visited
    


def count_distinct(visited: List[complex]) -> int:
    return len(set(visited))


@dataclass
class Tail:
    curr_loc = np.array((0, 0))
    visited = [np.array((0, 0))]

    @classmethod
    def count_visited(cls):
        return len(set(cls.visited))

    @staticmethod
    def in_proximity(coord1, coord2):
        i, j = coord1 - coord2
        if abs(i) <= 1 and abs(j) <= 1:
            return True
        else: 
            return False

    @classmethod
    def move(cls, target):
        # check if in proximity - do nothing if they are
        if cls.in_proximity(cls.curr_loc, target):
            return cls.curr_loc
                
        # check if difference is diagonal - both abs i & j != 0
        i, j = target - cls.curr_loc
        if i != 0 and j != 0:
            cls.curr_loc += np.sign((i, j))
            cls.visited.append(cls.curr_loc)

        # Recheck whether in proximity
        if cls.in_proximity(cls.curr_loc, target):
            return cls.curr_loc

        # keep moving T until H reached, updating visited and current coord (maybe batch)
        

        

        return cls.curr_loc
    
        
        


@dataclass
class Head:
    curr_loc = np.array((0, 0))

    UDLR = {
        'U': np.array((0, 1)), 
        'D': np.array((0, -1)), 
        'L': np.array((-1, 0)), 
        'R': np.array((1,0))
    }

    @classmethod
    def move(cls, direction, value):
        cls.curr_loc += cls.UDLR[direction] * value

    

    




if __name__ == '__main__':

    movements = create_input()

    visited = process_movements(movements)

    print(count_distinct(visited))