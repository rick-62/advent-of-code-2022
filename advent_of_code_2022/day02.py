from helper import load_input


def create_input():
    return load_input(2).readlines()


# A: [R]ock
# B: [P]aper
# C: [R]ock
# Y: [P]aper
# Z: [S]Scissors
# X: [c]issors

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






def calculate_score():
    pass

if __name__ == '__main__':
    lst = create_input()