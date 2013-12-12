from itertools import groupby
from operator import itemgetter


def main():
    sub = lambda x, y: x - y
    prods = sorted([(l.split(' ')[0], int(l.split(' ')[1])) for l in open('input.txt').read().splitlines()], key=itemgetter(0))
    [print(k, v) for k, v in [(k, sub(*map(itemgetter(1), g))) for k, g in groupby(prods, itemgetter(0))] if v != 0]


if __name__ == '__main__':
    main()