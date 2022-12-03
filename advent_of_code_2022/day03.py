from helper import load_input

def create_input():
    return load_input(3).readlines()


def split_string(string: str, n_chunks=2):

    len_chunk = int(len(string)/n_chunks)

    return [
        string[i:i+len_chunk] 
        for i in range(0, len(string), len_chunk)
    ]


def extract_common_letter(split_string):
    pass

# compare strings
# extract common letters
# prioritise & create score



if __name__ == '__main__':
    data = create_input()
    print(split_string('234532jgfusdjgn98g'))

