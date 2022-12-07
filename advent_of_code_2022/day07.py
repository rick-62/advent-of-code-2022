
import re

from typing import List

from helper import load_input


def create_input():
    return load_input(7).read()


def extract_dir_ls(terminal_output: str) -> List[str]:
    return re.findall(
        r'\$ ls\n(.*?)(?:\$|\Z)', 
        terminal_output,
        flags=re.S|re.M)


def extract_filesizes(dir_ls: str) -> List[int]:
    return [
        sum([int(x) for x in re.findall(r'(\d+)', ls)]) 
        for ls in dir_ls
    ]


def sum_fizesizes_lt_100000(filesizes: List[int]) -> int:
    return sum([x for x in filesizes if x <= 100_000])

    
if __name__ == '__main__':

    terminal_output = create_input()

    # Part 1
    dir_ls = extract_dir_ls(terminal_output)
    filesizes = extract_filesizes(dir_ls)
    print(sum_fizesizes_lt_100000(filesizes))

    print(filesizes)

