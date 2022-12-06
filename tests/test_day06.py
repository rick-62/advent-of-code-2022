from advent_of_code_2022 import day06

def test_create_input():
    assert type(day06.create_input()) is str


def test_no_dupes():
    assert day06.no_dupes('sdfg') == True
    assert day06.no_dupes('ssfg') == False


def test_index_where_no_dupes():
    assert day06.index_where_no_dupes('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7
    assert day06.index_where_no_dupes('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
    assert day06.index_where_no_dupes('nppdvjthqldpwncqszvftbrmjlhg') == 6
    assert day06.index_where_no_dupes('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
    assert day06.index_where_no_dupes('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11
    assert day06.index_where_no_dupes('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14) == 19
    assert day06.index_where_no_dupes('bvwbjplbgvbhsrlpgdmjqwftvncz', 14) == 23
    assert day06.index_where_no_dupes('nppdvjthqldpwncqszvftbrmjlhg', 14) == 23
    assert day06.index_where_no_dupes('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14) == 29
    assert day06.index_where_no_dupes('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14) == 26