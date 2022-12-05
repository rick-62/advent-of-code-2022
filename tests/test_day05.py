from advent_of_code_2022 import day05

def test_create_input():
    assert len(day05.create_input()) == 2


test_raw_stacks = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
"""

def test_initialise_stacks():
    assert day05.initialise_stacks(test_raw_stacks)[1] == ['Z', 'N']
    assert day05.initialise_stacks(test_raw_stacks)[2] == ['M', 'C', 'D']
    assert day05.initialise_stacks(test_raw_stacks)[3] == ['P']


def test_yield_procedure():
    assert next(day05.yield_procedure('move 1 from 2 to 1')) == [1, 2, 1]
    assert next(day05.yield_procedure('move 3 from 1 to 3')) == [3, 1, 3]
    assert next(day05.yield_procedure('move 2 from 2 to 1')) == [2, 2, 1]
    assert next(day05.yield_procedure('move 1 from 1 to 2')) == [1, 1, 2]

    test_input = day05.yield_procedure('move 1 from 1 to 2\nmove 2 from 2 to 1')
    assert next(test_input) == [1, 1, 2]
    assert next(test_input) == [2, 2, 1]


test_procedures = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def test_rearrange_crates():
    test_stacks = {
        1: ['Z', 'N'],
        2: ['M', 'C', 'D'],
        3: ['P'],
    }
    assert day05.rearrange_crates(test_procedures, test_stacks) == {
        1: ['C'],
        2: ['M'],
        3: ['P', 'D', 'N', 'Z'],
    }


def test_extract_top_crates():
    assert day05.extract_top_crates({
        1: ['C'],
        2: ['M'],
        3: ['P', 'D', 'N', 'Z'],
    }) == 'CMZ'


def test_rearrange_crates_9001():
    test_stacks = {
        1: ['Z', 'N'],
        2: ['M', 'C', 'D'],
        3: ['P'],
    }
    assert day05.rearrange_crates_9001(test_procedures, test_stacks) == {
        1: ['M'],
        2: ['C'],
        3: ['P', 'Z', 'N', 'D'],
    }