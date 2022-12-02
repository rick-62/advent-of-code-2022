from helper import load_input


def create_input():
    return load_input(2).read()


def standardise_input(
    data: str, 
    conversion = {'X': 'A', 'Y': 'B', 'Z': 'C'},
    ):

    data = data.replace(' ', '')

    for word, replacement in conversion.items():
        data = data.replace(word, replacement)

    return data.splitlines()


# RP: win (Paper beats Rock) = 6
# PS: win (Scissors beats Paper) = 6
# SR: win (Rock beats Scissors) = 6
# Draw occurs when equal = 3
# Otherwise it's a loss = 0

# Extra scores (no matter what)
# R: +1 
# S: +3 
# P: +2

# Assume Part 2 is finding the best assignment of X, Y, Z to get best score

def calculate_score(lines):
    
    scores = {
        # base
        'AB': 6,
        'BC': 6,
        'CA': 6,
        'AA': 3,
        'BB': 3,
        'CC': 3,
        # extras
        'A' : 1,
        'C' : 3,
        'B' : 2.
    }

    return int(sum([
        scores.get(play, 0) + scores.get(play[1]) 
        for play in lines
    ]))

# Part 2:
# X means you need to lose, 
# Y means you need to end the round in a draw, and 
# Z means you need to win


if __name__ == '__main__':
    data = create_input()

    # Part 1
    lines = standardise_input(data)
    part1 = calculate_score(lines)
    print(part1)

    # # Part 2
    lines = standardise_input(data,  conversion={
        'AX':'AC', 'AY':'AA', 'AZ':'AB',
        'BX':'BA', 'BY':'BB', 'BZ':'BC',
        'CX':'CB', 'CY':'CC', 'CZ':'CA'
    })
    part2 = calculate_score(lines)
    print(part2)


