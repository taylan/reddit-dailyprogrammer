from itertools import zip_longest


def print_line(line):
    print("".join([char if char is not None else " " for char in line]))


def main():
    inp = open("input.txt").read().splitlines()

    # readable
    for line in list(zip_longest(*inp[1:])):
        print("".join([char if char is not None else " " for char in line]))

    # slightly less readable
    list(map(print_line, list(zip_longest(*inp[1:]))))

    #even less readable
    list(map(lambda line : print("".join([char if char is not None else " " for char in line])), list(zip_longest(*open("input.txt").read().splitlines()[1:]))))

if __name__ == "__main__":
    main()