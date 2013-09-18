import random
from itertools import zip_longest

def get_operation(a, b):
    ops = ['+', '-', '*']
    random.shuffle(ops)
    nums = [str(random.randint(a, b)) for i in list(range(4))]

    tups = zip_longest(nums, ops)
    return " ".join([item for tup in tups for item in tup if item is not None]) #interleave ops and nums, and extract items from list of tuples

def main():
    while True:
        print("> Enter two integers: ")
        inp = input()
        if inp.lower() == 'q':
            break

        op = get_operation(*[int(i) for i in inp.split(' ')][:2])
        print("> op: {0}".format(op))
        user_result = input()
        if user_result.lower() == 'q':
            break

        user_result_is_correct = eval(op) == int(user_result)
        print("correct!" if user_result_is_correct else "incorrect...")


if __name__ == "__main__":
    main()