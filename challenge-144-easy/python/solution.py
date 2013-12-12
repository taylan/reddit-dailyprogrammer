from operator import itemgetter


def main():
    sub = lambda x, y: int(x) - int(y)
    sort = lambda l: sorted(l, key=itemgetter(0))
    lines = [l.split(' ') for l in open('input.txt').read().splitlines()]
    changes = [(k[0][0], sub(*map(itemgetter(1), k))) for k in
             (zip(sort(lines[:len(lines) // 2]), sort(lines[len(lines) // 2:])))]
    [print(prod, difference) for prod, difference in changes if difference != 0]


if __name__ == '__main__':
    main()