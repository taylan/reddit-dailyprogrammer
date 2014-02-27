from itertools import tee, filterfalse


def solution1(s):
    vow = []
    dis = []
    for c in s.replace(' ', ''):
        (vow if c in ['a', 'e', 'i', 'o', 'u'] else dis).append(c)

    print(''.join(dis))
    print(''.join(vow))


def solution2(s):
    t1, t2 = tee(s.replace(' ', ''))
    isvow = lambda x: x in ['a', 'e', 'i', 'o', 'u']
    dd, vv = filterfalse(isvow, t1), filter(isvow, t2)

    print(''.join(dd))
    print(''.join(vv))


def main():
    s = 'all those who believe in psychokinesis raise my hand'
    solution1(s)
    solution2(s)


if __name__ == '__main__':
    main()
