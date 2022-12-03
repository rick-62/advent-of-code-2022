from helper import load_input
from itertools import combinations
import string

def create_input():
    return load_input(3).read().replace('\n', ' ').split()


def split_into_chunks(string: str, n_chunks=2):
    '''split string evenly into n chunks''' 

    len_chunk = int(len(string)/n_chunks)

    return [
        string[i:i+len_chunk] 
        for i in range(0, len(string), len_chunk)
    ]


def extract_common_items(compartments):

    # convert strings to sets
    sets = [set(chunk) for chunk in compartments]

    # identify common letters
    intersection = [a & b for a, b in combinations(sets, 2)]

    # return distinct list of common letters
    return ''.join(set.union(*intersection))




def calculate_total_score(bags):

    common_items = ''.join([extract_common_items(split_into_chunks(bag)) for bag in bags])

    print(common_items)

    return sum([string.ascii_letters.index(item) + 1 for item in common_items])


    



# prioritise & create score



if __name__ == '__main__':
    bags = create_input()
    print(split_into_chunks('234532jgfjjusdjgn98g'))
    print(extract_common_items(['234532jgf', 'jusdjgn98']))
    print(calculate_total_score(bags))
