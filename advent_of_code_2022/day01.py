import heapq

from helper import load_input



def create_input():
    '''read in puzzle input from file & prep'''
    chunks = load_input(1).read().split('\n\n')
    return [chunk.splitlines() for chunk in chunks]


def sum_calories_from_each_chunk(rations):
    return [sum([int(calories) for calories in food]) for food in rations]


def max_calories(total_calories, n=1):
    return sum(heapq.nlargest(n, total_calories))


if __name__ == '__main__':

    rations = create_input()
    total_calories = sum_calories_from_each_chunk(rations)
    print(max_calories(total_calories))
    print(max_calories(total_calories, 3))

    
