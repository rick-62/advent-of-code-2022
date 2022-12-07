from advent_of_code_2022 import day07


def test_create_input():
    assert type(day07.create_input()) is str


terminal_output = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


def test_extract_dir_ls():
    assert type(day07.extract_dir_ls(terminal_output)) == list
    assert len(day07.extract_dir_ls(terminal_output)) == 4
    assert day07.extract_dir_ls(terminal_output)[2] == '584 i\n'
    assert day07.extract_dir_ls(terminal_output)[1] == 'dir e\n29116 f\n2557 g\n62596 h.lst\n'


def test_extract_filesizes():
    assert day07.extract_filesizes(['dir e\n29116 f\n2557 g\n62596 h.lst\n']) == [94269]
    assert day07.extract_filesizes(['dir e\n29116 f\n2557 g\n62596 h.lst\n', '45']) == [94269, 45]
    assert set(day07.extract_filesizes(day07.extract_dir_ls(terminal_output))) == set([48381165, 94853, 584, 24933642])


def test_sum_filesizes_lt_100000():
    assert day07.sum_fizesizes_lt_100000([123, 134555, 6]) == 129

