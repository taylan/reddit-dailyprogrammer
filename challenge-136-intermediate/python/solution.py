from itertools import groupby


def _calc_tally(tally, candidates, votes, rnd):
    for v in votes:
        tally[candidates[v[rnd]]] += 1
    return tally


def main():
    inp = open('input.txt').read().splitlines()
    candidates = inp[0].split(' ')
    votes = [list(map(int, l.split(' '))) for l in inp[1:]]
    tally = {c: 0 for c in candidates}
    rnd = 0

    while rnd < len(candidates) and not any(vc > len(votes) / 2 for vc in tally.values()):
        rnd += 1
        if rnd == 1:
            tally = _calc_tally(tally, candidates, votes, rnd-1)
        else:
            loser = sorted(tally.items(), key=lambda t: t[1])[0][0]
            tally.pop(loser)
            tally = _calc_tally(tally, candidates, filter(lambda v: v[0] == candidates.index(loser), votes), rnd-1)

        print('Round {0}: {1}'.format(rnd, ', '.join(['{0:.02f}% {1}'.format(x[1]/len(votes) * 100, x[0]) for x in sorted(tally.items(), key=lambda t: t[1], reverse=True)])))

    winners = [c[0] for c in sorted(list(groupby(tally.items(), lambda x: x[1])), key=lambda x: x[0], reverse=True)[0][1]]
    print('{0} {1} after {2} round{3}.'.format('Winner is' if len(winners) == 1 else 'Result is a draw. Winners are', ', '.join(winners), rnd, '' if rnd == 1 else 's'))


if __name__ == '__main__':
    main()