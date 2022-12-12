
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



def test_process_movements():

    assert day09.process_movements(['R 4']) == [0, 1, 2, 3]
    assert day09.process_movements(test_input1) == [
        0, 1, 2, 3,         # R 4
        4+1j, 4+2j, 4+3j,   # U 4
        3+4j, 2+4j,         # L 3
                            # D 1
        3+3j, 4+3j,         # R 4
        ]


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

    assert day09.finish_moving_tail('R', tail=0+0j, head=2+0j) == [1+0j]
    assert day09.finish_moving_tail('R', tail=0+0j, head=1+0j) == []
    assert day09.finish_moving_tail('U', tail=0+0j, head=0+5j) == [1j, 2j, 3j, 4j]
    assert day09.finish_moving_tail('D', tail=0+0j, head=0-5j) == [-1j, -2j, -3j, -4j]
    assert day09.finish_moving_tail('L', tail=0+0j, head=-5+0j) == [-1, -2, -3, -4]
    assert day09.finish_moving_tail('U', tail=2-2j, head=2+0j) == [2-1j]












