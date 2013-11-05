from re import sub
from itertools import groupby


def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for line in [l.lower() for l in open('input.txt').read().splitlines()]:
        letters = list(sub('[^{0}]'.format(alphabet), '', line))
        distinct_letters = list(set(letters))
        print(str(len(distinct_letters) == len(alphabet)), ', '.join(['{0}: {1}'.format(k, len(list(g))) for k, g in groupby(sorted(letters))]))


if __name__ == '__main__':
    main()