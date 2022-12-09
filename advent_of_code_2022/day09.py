
from typing import Tuple

from helper import load_input


def create_input():
    return load_input(9).read().splitlines()


def move_tail_coords(h_coord: Tuple[int], t_coord: Tuple[int]) -> (Tuple[int], set[Tuple[int]]):
    '''
    Given the new Head coords, move Tail coords accordingly.
    Returns set of visited coordinates & final position of Tail.
    '''
    pass

# Ue objects instead? Tidier than moving coords around etc
# given both coorinates, return list of coordinates Tail has followed
# for instruction, move H -> update coord, update Tail coords
    # add to set all T coordss
# finally count the length of the set to get puzzle answer


if __name__ == '__main__':

    pass