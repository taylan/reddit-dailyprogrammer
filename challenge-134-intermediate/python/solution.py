
def denominate(amt, coins):
    denoms = dict()
    for c in sorted(coins, reverse=True):
        d, amt = divmod(amt, c)
        denoms[c] = d
        if amt == 0:
            break

    return ' '.join(['{0}:{1}'.format(k, v) for k, v in denoms.items()])


def main():
    valstr, *coins = open('input.txt').read().splitlines()
    for c in coins:
        print(denominate(int(valstr), list(filter(lambda x: x < int(valstr), map(int, c.split(' '))))))


if __name__ == '__main__':
    main()