
import numpy as np

from advent_of_code_2022 import day09


def test_create_input():
    assert len(day09.create_input()) > 5



test_input1 = [
    'R 4',
    'U 4',
    'L 3',
    'D 1',
    'R 4',
]

test_input2 = [
    'R 5',
    'U 8',
    'L 8',
    'D 3',
    'R 17',
    'D 10',
    'L 25',
    'U 20',
]


def test_get_head_coords():

    assert list(day09.get_head_coord(['R 4'])) == [1, 2, 3, 4]
    assert list(day09.get_head_coord(['R 4', 'U 4'])) == [1, 2, 3, 4, 4+1j, 4+2j, 4+3j, 4+4j]
    assert list(day09.get_head_coord(['R 4', 'U 4', 'L 3', 'D 1'])) == [
        1, 2, 3, 4,                 # R 4
        4+1j, 4+2j, 4+3j, 4+4j,     # U 4
        3+4j, 2+4j, 1+4j,           # L 3
        1+3j,                       # D 1
    ]


def test_process_movements():

    # Part 1 - one tail
    assert day09.process_movements(['R 4'], n_tails=1) == [0, 1, 2, 3]
    assert day09.process_movements(test_input1, n_tails=1) == [
        0, 1+0j, 2+0j, 3+0j,  # R 4
        4+1j, 4+2j, 4+3j,     # U 4
        3+4j, 2+4j,           # L 3
                              # D 1
        3+3j, 4+3j,           # R 4
        ]

    # two tails
    assert day09.process_movements(['R 4'], n_tails=2) == [0, 1+0j, 2+0j]
    assert day09.process_movements(['R 4', 'U 4'], n_tails=2) == [
        0, 1+0j, 2+0j,
        3+1j, 4+2j,
    ]
    assert day09.process_movements(['R 4', 'U 4', 'L 3'], n_tails=2) == [
        0, 1+0j, 2+0j,
        3+1j, 4+2j,
        3+3j, 
    ]


def test_count_distinct():

    visited = day09.process_movements(test_input2)
    assert day09.count_distinct(visited) == 36


def test_in_proximity_method():

    # TRUE outcomes
    assert day09.in_proximity(0+0j) == True
    assert day09.in_proximity(1+0j) == True
    assert day09.in_proximity(0+1j) == True
    assert day09.in_proximity(-1+0j) == True
    assert day09.in_proximity(1+1j) == True
    assert day09.in_proximity(-1-1j) == True

    # FALSE outcomes
    assert day09.in_proximity(-1-5j) == False
    assert day09.in_proximity(-5-5j) == False
    assert day09.in_proximity(1+2j) == False
    assert day09.in_proximity(2-1j) == False
    assert day09.in_proximity(0-5j) == False
    assert day09.in_proximity(0+2j) == False


def test_complex_sign():

    assert day09.complex_sign(6+4j) == 1+1j
    assert day09.complex_sign(-5+4j) == -1+1j
    assert day09.complex_sign(-6+-4j) == -1-1j
    assert day09.complex_sign(-6+0j) == -1+0j
    assert day09.complex_sign(6+-4j) == 1-1j


def test_finish_moving_tail():

    assert day09.finish_moving_tail(tail=0+0j, head=2+0j) == [1+0j]
    assert day09.finish_moving_tail(tail=0+0j, head=1+0j) == []
    assert day09.finish_moving_tail(tail=0+0j, head=0+5j) == [1j, 2j, 3j, 4j]
    assert day09.finish_moving_tail(tail=0+0j, head=0-5j) == [-1j, -2j, -3j, -4j]
    assert day09.finish_moving_tail(tail=0+0j, head=-5+0j) == [-1, -2, -3, -4]
    assert day09.finish_moving_tail(tail=2-2j, head=2+0j) == [2-1j]
    assert day09.finish_moving_tail(tail=3+4j, head=1+4j) == [2+4j]


def test_process_movement():

    assert day09.process_movement(head=-5+0j, tail=0+0j) == [-1, -2, -3, -4]
    assert day09.process_movement(head=-5+1j, tail=0+0j) == [-1+1j, -2+1j, -3+1j, -4+1j]
    assert day09.process_movement(tail=0+0j, head=1+0j) == []
    assert day09.process_movement(tail=0+0j, head=2+0j) == [1+0j]
    assert day09.process_movement(tail=0+0j, head=2+1j) == [1+1j]







