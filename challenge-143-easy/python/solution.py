def main():
    braille_dict = dict([l.split(' ') for l in open('dict.txt').read().splitlines()])
    print(''.join(map(braille_dict.get, map(lambda x: ''.join(x), zip(
        *[l.split(' ') for l in open('input.txt').read().splitlines()])))))


if __name__ == '__main__':
    main()