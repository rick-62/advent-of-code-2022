
from dataclasses import dataclass
from typing import Tuple

import numpy as np

from helper import load_input


def create_input():
    return load_input(9).read().splitlines()


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

    

    



    

    



# def move_tail_coords(h_coord: Tuple[int], t_coord: Tuple[int]) -> (Tuple[int], set[Tuple[int]]):
#     '''
#     Given the new Head coords, move Tail coords accordingly.
#     Returns set of visited coordinates & final position of Tail.
#     '''
#     pass

# given both coordinates, return list of coordinates Tail has followed
# for instruction, move H -> update coord, update Tail coords
    # add to set all T coordss
# finally count the length of the set to get puzzle answer


if __name__ == '__main__':

    pass