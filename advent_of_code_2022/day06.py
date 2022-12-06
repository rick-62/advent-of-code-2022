
from helper import load_input

def create_input():
    return load_input(6).read()


def no_dupes(string4: str) -> bool:
    return len(set(string4)) == len(string4)


def index_where_no_dupes(string: str, chars=4) -> int:
    for i in range(len(string)-chars):
        if no_dupes(string[i:i+chars]):
            return i + chars


if __name__ == '__main__':

    string = create_input()

    # Part 1
    print(index_where_no_dupes(string))

    # Part 2
    print(index_where_no_dupes(string, 14))
