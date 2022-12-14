
from typing import Dict

from helper import load_input


def create_input():
    return load_input(10).read().splitlines()


# clock circuit cycle
# CPU register X = 1
# two instructions;
    # addx V (2 cyles to complete) AFTER two cycles X += V
    # noop (1 cylce to complete) with not other effect.
# CPU uses input to draw on screen
def process_program(instructions):
    record = {0: 1}
    cycle = 0
    X = 1
    for instruction in instructions:
        if instruction == 'noop':
            cycle += 1
        elif instruction.split()[0] == 'addx':
            cycle += 2
            X += int(instruction.split()[1])
            record[cycle] = X
        else:
            raise Exception(instruction)
    return record


# signal strength
# cycle number times X
# DURING 20th cycle & every 40 cycles after that
def calc_signal_strength(record: Dict[int, int]):
    score = 0
    for cycle in [20, 60, 100, 140, 180, 220]:
        i = list(filter(lambda x: x < cycle, record.keys()))[-1]
        X = record[i]
        score += cycle * X
    return score

    
# X controls the location of a sprite 3 pixel wide ###
# if cycle number overlaps any part of the sprite then the pixel is lit #, else .
# 6 rows: cycles 1-40, 41-80 ... 201-240
# print the resulting image
def process_image(records: Dict[int, int]):
    rows = [
        (1,40), 
        (41,80),
        (81,120),
        (121,160),
        (161,200),
        (201,240),
    ]
    for row in rows:
        start, end = row
        for column in range(40):
            cycle = start + column
            i = list(filter(lambda x: x < cycle, records.keys()))[-1]
            X = records[i]
            if column in range(X-1, X+2):
                print('#', end='')
            else:
                print('.', end='')
        print()
        

if __name__ == '__main__':

    instructions = create_input()

    # Part 1
    record = process_program(instructions)
    print(calc_signal_strength(record))

    # Part 2
    process_image(record)