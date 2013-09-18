import random
from itertools import zip_longest

def get_operation(a, b):
    ops = ['+', '-', '*']
    random.shuffle(ops)
    nums = [str(random.randint(a, b)) for i in list(range(4))]

    tups = zip_longest(nums, ops)
    return " ".join([item for tup in tups for item in tup if item is not None]) #interleave ops and nums, then extract items from list of tuples

def main():
    while True:
        print("> Enter two integers: ")
        inp = input()
        if inp.lower() == 'q':
            print("exiting. bye!")
            break
        try:
            params = [int(i) for i in inp.split(' ')]
            print(params)
            if len(params) != 2:
                raise Exception
        except:
            print("You need to enter two integers")
            continue

        op = get_operation(*params)
        print("> op: {0}".format(op))
        print("> enter result: ")
        user_result = input()
        if user_result.lower() == 'q':
            print("exiting. bye!")
            break

        try:
            user_result_is_correct = eval(op) == int(user_result)
            print("correct!" if user_result_is_correct else "incorrect...")
        except:
            print("> try again!")


if __name__ == "__main__":
    main()