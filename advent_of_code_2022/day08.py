import os

from itertools import product, takewhile
from typing import Tuple, Iterable

import numpy as np

from helper import load_input


def create_input(fname: str):
    return np.genfromtxt(fname, dtype=int, delimiter=1)


def is_tree_visible(arr, ij: Tuple[int]) -> bool:
    '''
    checks whether single tree is visible from ground level
        - arr is the tree map (puzzle input)
        - ij is the tree coordinate
    '''
    i, j = ij   

    # are coordinates on the edge of the array (these are visible)
    if i == 0 or j == 0 or (i == arr.shape[0] - 1) or (j == arr.shape[1] - 1):
        return True

    tree_height = arr[i,j]

    # check visibilty from the North
    if tree_height > max(arr[0:i, j]):
        return True

    # check visibilty from the South
    if tree_height > max(arr[i+1:, j]):
        return True

    # check visibilty from the East
    if tree_height > max(arr[i, j+1:]):
        return True

    # check visibilty from the West
    if tree_height > max(arr[i, 0:j]):
        return True

    return False


def count_visible_trees(tree_map):
    '''counts number of trees visible from all directions'''
    coords = product(range(tree_map.shape[0]), range(tree_map.shape[1]))
    return sum([is_tree_visible(tree_map, ij) for ij in coords])


def score_line_of_sight(tree_height: int, trees: Iterable[int]) -> int:
    '''counts the number of visible trees in line of sight'''
    base_score = len(list(takewhile(lambda x: x < tree_height, trees)))
    if max(trees) >= tree_height:
        return base_score + 1
    else:
        return base_score


def calculate_tree_scenic_score(arr, ij: Tuple[int]) -> int:
    '''calculates tree scenic score by multipling visible trees'''
    i, j = ij 
    tree_height = arr[i,j]

    # are coordinates on the edge of the array (score 0)
    if i == 0 or j == 0 or (i == arr.shape[0] - 1) or (j == arr.shape[1] - 1):
        return 0
    
    # score the different lines of sight
    north = score_line_of_sight(tree_height, arr[0:i, j][::-1])
    south = score_line_of_sight(tree_height, arr[i+1:, j])
    east = score_line_of_sight(tree_height, arr[i, j+1:])
    west = score_line_of_sight(tree_height, arr[i, 0:j][::-1])

    return north * south * west * east
        

def find_best_scoring_tree(tree_map):
    coords = product(range(tree_map.shape[0]), range(tree_map.shape[1]))
    return max([calculate_tree_scenic_score(tree_map, ij) for ij in coords])


if __name__ == '__main__':

    tree_map = create_input(os.path.join('inputs', 'day08.txt'))

    # Part 1
    print(count_visible_trees(tree_map))

    # Part 2
    print(find_best_scoring_tree(tree_map))