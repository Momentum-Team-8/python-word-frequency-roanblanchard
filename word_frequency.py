
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with', '\n', ''
]


words = {}


punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~-'''


def print_word_freq(file):
    file = open(file, "r")
    read_file = file.readlines()
    for i in read_file:
        x = i.split()
        for i in x:
            # print(i)
            if i[-1] in punc:
                i = i.replace(i, i[0:-1])
            if i in STOP_WORDS:
                pass
            elif i in words:
                words[i] += 1
            else:
                i = i.lower()
                words[i] = 1
    print(sorted(words, key=words.get, reverse=True))

    file.close()


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
