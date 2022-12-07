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


sample_terminal_output1 = \
"""
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
"""

sample_terminal_output2 = \
"""
$ cd /
$ ls
dir a
$ cd a
$ ls
dir a
2 a.txt
$ cd a
$ ls
99999 a.txt
"""

def test_create_dir_store():

    store, dirs = day07.create_dir_store(sample_terminal_output1) 
    assert store == {'/': 23352670, '/-a': 94269}
    assert dirs == set(['/', '/-a'])

    store, dirs = day07.create_dir_store(terminal_output) 
    assert store == {'/': 23352670, '/-a': 94269, '/-a-e': 584, '/-d': 24933642}
    assert dirs == set(['/', '/-a', '/-a-e', '/-d'])

    store, dirs = day07.create_dir_store(sample_terminal_output2)
    assert store == {'/-a': 2, '/-a-a': 99999}


def test_tally_each_dir():
    
    assert day07.tally_each_dir(set(['/','/-a']), {'/': 23352670, '/-a': 94269}) == {
        '/': 23352670 + 94269,
        '/-a': 94269
    }

    assert day07.tally_each_dir(
        set(['/', '/-a', '/-a-e', '/-d']), 
        {'/': 23352670, '/-a': 94269, '/-a-e': 584, '/-d': 24933642}) == {
            '/': 48381165,
            '/-a': 94853 ,
            '/-a-e': 584,
            '/-d': 24933642
        }
 


def test_sum_dirsizes_lt_100000():
    assert day07.sum_dirsizes_lt_100000({'/': 23352670 + 94269, 'a': 94269}) == 94269
    assert day07.sum_dirsizes_lt_100000({
        '/': 23352670 + 94269 + 24933642 + 584,
        'a': 94269 + 584,
        'e': 584,
        'd': 24933642
    }) == 95437
    

def test_calc_space_required():
    assert day07.calc_space_required(48381165) == 8381165



def test_size_of_smallest_dir_to_remove():
    assert day07.size_of_smallest_dir_to_remove(
        {
            '/': 48381165,
            '/-a': 94853 ,
            '/-a-e': 584,
            '/-d': 24933642
        }
    ) == 24933642