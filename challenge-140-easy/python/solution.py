from string import capwords


def main():
    ops = [lambda x: capwords(x), lambda x: x.lower(), lambda x: x.upper()]
    for p in [l.split(' ') for l in open('input.txt').read().splitlines()]:
        print(('' if p[0] == '0' else '_').join(list(map(ops[int(p[0])], p[1:]))))


if __name__ == '__main__':
    main()