
from advent_of_code_2022 import day11


def test_create_input():
    assert len(day11.create_input()) == 8


def test_Monkey():

    monkey = day11.Monkey('1', '79, 63', '* 19', '5', '0', '3')

    assert monkey.monkey == 1
    assert monkey.items == [79, 63]
    assert eval(monkey.operation.format(79)) == 1501
    assert monkey.test == 5
    assert monkey.true == 0
    assert monkey.false == 3

    assert monkey.inspect_item() == (0, 500)
    assert monkey.inspect_item() == (3, 399)


def test_create_monkeys():

    monkeys = day11.create_monkeys(['''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3'''])

    assert monkeys[0].monkey == 0
    assert monkeys[0].items == [79, 98]
    assert monkeys[0].test == 23
    assert monkeys[0].true == 2






