
import numpy as np

from advent_of_code_2022 import day09


def test_create_input():
    assert len(day09.create_input()) > 5


def test_Head():
    
    day09.Head.move('R', 4)
    assert list(day09.Head.curr_loc) == [4,0]

    day09.Head.move('U', 4)
    assert list(day09.Head.curr_loc) == [4,4]

    day09.Head.move('L', 3)
    assert list(day09.Head.curr_loc) == [1,4]

    day09.Head.move('D', 1)
    assert list(day09.Head.curr_loc) == [1,3]

    day09.Head.move('R', 4)
    day09.Head.move('D', 1)
    day09.Head.move('L', 5)
    day09.Head.move('R', 2)
    assert list(day09.Head.curr_loc) == [2,2]


def test_Tail():

    assert list(day09.Tail.move((1, 1))) == [0, 0]
    assert list(day09.Tail.move((1, 2))) == [1, 1]
    assert list(day09.Tail.move((1, 3))) == [1, 2]


    # Test count of visited
    day09.Tail.visited = []
    assert day09.Tail.count_visited() == 0
    day09.Tail.visited = [(0, 0),(1, 0),(0, 5),(2, 0),(0, 0),]
    assert day09.Tail.count_visited() == 4


def test_in_proximity_method():

    # positive coords
    assert day09.Tail.in_proximity(np.array((0, 0)), np.array((1, 3))) == False
    assert day09.Tail.in_proximity(np.array((1, 1)), np.array((1, 3))) == False
    assert day09.Tail.in_proximity(np.array((1, 4)), np.array((1, 3))) == True
    assert day09.Tail.in_proximity(np.array((2, 4)), np.array((1, 3))) == True

    # negative coords
    assert day09.Tail.in_proximity(np.array((2, 4)), np.array((-1, -3))) == False
    assert day09.Tail.in_proximity(np.array((-2, -4)), np.array((-1, -3))) == True
    assert day09.Tail.in_proximity(np.array((0, -3)), np.array((-1, -3))) == True








