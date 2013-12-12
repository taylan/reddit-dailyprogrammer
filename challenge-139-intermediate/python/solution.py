def get_keys():
    keys = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    keypad = dict()
    for i, k in enumerate(keys):
        keypad.update({str(i+2)*(k.index(c)+1): c for c in k})
    return keypad


def find_words(words, q):
    return [w for w in words if w.startswith(q)]


def main():
    dic = [w for w in open('dict.txt').read().splitlines()]
    keypad = get_keys()
    [print(w) for w in find_words(dic, ''.join(map(keypad.get, '7777 666 555 3'.split(' '))))]


if __name__ == '__main__':
    main()