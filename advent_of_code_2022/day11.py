
import heapq
import re

from typing import List

from helper import load_input


def create_input():
    return load_input(11).read().split('\n\n')


REGEX = re.compile(r'Monkey (\d+):\n  Starting items: (.+)\n  Operation: new = old (.+)\n  Test: divisible by (\d+)\n    If true: throw to monkey (\d+)\n    If false: throw to monkey (\d+)')


# starting items list worry level for each item
# Operation is how worry level changes for item as inspected by monkey
# For all monkeys, once inspected divide by 3 and round to nearest integer
# Test based on worry level determines where monkey will throw next
# if true throw to monkey x; if false throw to monkey y
# items are consumed from first to last, with new items getting appended i.e. pop(0)
# items retain their new worry level
class Monkey:

    def __init__(self, monkey, items, operation, test, true, false):
        self.monkey = int(monkey)
        self.items = [int(i) for i in items.split(',')]
        self.operation = '{} ' + operation
        self.test = int(test)
        self.true = int(true)
        self.false = int(false)
        self.count = 0
        self.print = False
        self.part2 = False


    def inspect_item(self):
        old = self.items.pop(0)
        if self.print: print(f"\tMonkey inspects an item with a worry level of {old}.")

        self.count += 1

        new = eval(self.operation.format(old))
        if self.print: print(f"\t\tWorry level is calculated to {new}.")

        new = int(new / 3) if not self.part2 else new
        if self.print: print(f"\t\tMonkey gets bored with item. Worry level is divided by 3 to {new}.")

        if new % self.test == 0:
            if self.print: print(f"\t\tCurrent worry level is divisible by {self.test}.")
            if self.print: print(f"\t\tItem with worry level {new} is thrown to monkey {self.true}.")
            return (self.true, new)
        else:
            if self.print: print(f"\t\tCurrent worry level is not divisible by {self.test}.")
            if self.print: print(f"\t\tItem with worry level {new} is thrown to monkey {self.false}.")
            return (self.false, new)


    def inspect_items(self):
        if self.print: print(f"Monkey {self.monkey}:")

        for _ in range(len(self.items)):
            yield self.inspect_item()


def create_monkeys(raw_data: List[str]) -> Monkey:
    return [Monkey(*REGEX.match(m).groups()) for m in raw_data]


def print_monkey_items(monkeys):
    for i, monkey in enumerate(monkeys):
        print(f"Monkey {i}({monkey.monkey}): {monkey.items}")

def debug_monkeys(monkeys):
    for monkey in monkeys:
        monkey.print = True

def part2_monkeys(monkeys):
    for monkey in monkeys:
        monkey.part2 = True

# during a round
# monkeys take turns inspecting all their items
# if monkey holds no items then their turn immediately ends
def play_round(monkeys):
    for monkey in monkeys:
        for i, item in monkey.inspect_items():
            monkeys[i].items.append(item)
    # print_monkey_items(monkeys)
    return monkeys


# focus on two most active monkeys
# total number of times each monkey inspects items
# multiply times top two active monkeys inspect items
# what is level of "monkey business" after 20 rounds?
def play_rounds(monkeys, n_rounds):
    for _ in range(n_rounds):
        monkeys = play_round(monkeys)
    return monkeys


def calc_score(monkeys):
    x, y = heapq.nlargest(2, [m.count for m in monkeys])
    return x * y


if __name__ == '__main__':

    raw_data = create_input()

    # Part 1
    monkeys = create_monkeys(raw_data)
    # debug_monkeys(monkeys)
    play_rounds(monkeys, 20)
    print(calc_score(monkeys))

    # Part 2
    monkeys = create_monkeys(raw_data)
    part2_monkeys(monkeys)
    play_rounds(monkeys, 100)
    print(calc_score(monkeys))
