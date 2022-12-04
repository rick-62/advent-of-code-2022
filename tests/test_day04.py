from advent_of_code_2022 import day04


def test_create_input():
    assert len(day04.create_input()) > 10
    assert type(day04.create_input()) == list


def test_check_section_overlap():
    assert day04.check_section_overlap('2-4,6-8') == False
    assert day04.check_section_overlap('6-6,6-8') == True
    assert day04.check_section_overlap('2-8,3-7') == True
    assert day04.check_section_overlap('20-40,1,5') == False
    assert day04.check_section_overlap('100-125,110-115') == True
    assert day04.check_section_overlap('5-7,7-9', day04.partial_overlap) == True
    assert day04.check_section_overlap('2-8,3-7', day04.partial_overlap) == True
    assert day04.check_section_overlap('6-6,4-6', day04.partial_overlap) == True
    assert day04.check_section_overlap('2-6,4-8', day04.partial_overlap) == True


input_list = [
    '2-4,6-8',
    '2-3,4-5',
    '5-7,7-9',
    '2-8,3-7',
    '6-6,4-6',
    '2-6,4-8',
]

def test_sum_overlap():
    assert day04.sum_overlap(input_list, day04.full_overlap) == 2
    assert day04.sum_overlap(input_list, day04.partial_overlap) == 4

