
import numpy as np

from advent_of_code_2022 import day09


def test_create_input():
    assert len(day09.create_input()) > 5




def test_process_movements():

    day09.process_movements(['R 4'])


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










