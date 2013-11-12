from random import shuffle, choice


def main():
    sims = 100000
    num_str1 = 0
    num_str2 = 0

    for i in range(0, sims):
        doors = [0, 0, 1]
        shuffle(doors)
        user_choice = doors[choice(list(range(0, 3)))]
        if user_choice == 1:
            num_str1 += 1
        else:
            num_str2 += 1

    print('Strategy 1 win percentage: {0:.0f}%, Strategy 2 win percentage: {1:.0f}%'.format(num_str1 / sims * 100, num_str2 / sims * 100))


if __name__ == '__main__':
    main()