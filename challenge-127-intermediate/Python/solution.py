def initialize(entries, day):
    forwards = dict()

    for entry in entries:
        frm, to = entry.split(' ')[:2]
        start, length = list(map(int, entry.split(' ')[2:]))
        # filter forwards which do not occur on the target day
        if not start <= day <= start + length:
            continue

        forward = forwards.get(frm, [])
        forward.append({
            'dest': to,
            'ts': start,
            'te': start + length
        })
        forwards[frm] = forward

    return forwards


def get_max_forward_chain_count(redirects, visited, source, day):
    if source not in redirects:
        return 0

    if source in visited:
        raise RuntimeError("Cyclical forwarding on path {0} with last forward to {1}".format(visited, source))

    visited.add(source)

    forwards = [f for f in redirects[source]]
    if len(forwards) == 0:
        return 0

    return 1 + max([get_max_forward_chain_count(redirects, visited, f['dest'], day) for f in forwards])


def calculate_forward_chain_lengths(redirects, day):
    max_chain_counts = dict()
    for source in redirects.keys():
        try:
            max_chain_counts[source] = get_max_forward_chain_count(redirects, set(), source, day)
        except RuntimeError as re:
            print(re)
            exit(1)

    return max_chain_counts


def main():
    with open('input.txt') as input_file:
        num_forw, *forwards, day = input_file.read().splitlines()

    forwards = initialize(forwards, int(day))

    print("{0} call forwardings set up on day 2".format(len([x for f in forwards.values() for x in f]), day))
    print("{0} call forwardings are the longest chain on day {1}".format(max(list(calculate_forward_chain_lengths(forwards, int(day)).values())), day))


if __name__ == '__main__':
    main()