
import os

from advent_of_code_2022 import day08


sample_map = \
"""
30373
25512
65332
33549
35390
"""

arr = day08.create_input(os.path.join('inputs', 'test_day08.txt')) 


def test_create_input():
    assert arr[0,0] == 3
    assert max(arr[0]) == 7
    assert min(arr[0]) == 0
    assert max(arr[-1]) == 9
    assert arr[2,4] == 2
    assert arr.shape == (5,5)


def test_is_tree_visible():
    assert day08.is_tree_visible(arr, (0, 2)) == True
    assert day08.is_tree_visible(arr, (4, 4)) == True
    assert day08.is_tree_visible(arr, (1, 2)) == True
    assert day08.is_tree_visible(arr, (3, 3)) == False
    assert day08.is_tree_visible(arr, (2, 2)) == False
    assert day08.is_tree_visible(arr, (3, 1)) == False
    assert day08.is_tree_visible(arr, (0, 0)) == True
    assert day08.is_tree_visible(arr, (4, 4)) == True
    assert day08.is_tree_visible(arr, (1, 3)) == False


def test_count_visible_trees():
    assert day08.count_visible_trees(arr) == 21


def test_score_line_of_sight():
    assert day08.score_line_of_sight(5, [3, 5, 3]) == 2
    assert day08.score_line_of_sight(5, [3, 3]) == 2
    assert day08.score_line_of_sight(5, [5]) == 1


def test_calculate_tree_scenic_score():
    assert day08.calculate_tree_scenic_score(arr, (3, 2)) == 8
    assert day08.calculate_tree_scenic_score(arr, (1, 2)) == 4
    assert day08.calculate_tree_scenic_score(arr, (1, 1)) == 1 * 1 * 1 * 1
    assert day08.calculate_tree_scenic_score(arr, (2, 1)) == 1 * 1 * 3 * 2
    assert day08.calculate_tree_scenic_score(arr, (3, 3)) == 3 * 1 * 1 * 1
    

def test_find_best_scoring_tree():
    assert day08.find_best_scoring_tree(arr) == 8



