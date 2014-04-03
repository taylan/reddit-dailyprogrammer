opn = ['(', '{', '[']
cls = [')', '}', ']']
s = '[racket for brackets (matching) is a} computers]'

stk = []
for i, c in enumerate(s):
    if c in opn:
        stk.append(c)
    elif c in cls:
        prev = stk.pop() if stk else None
        if not prev:
            print('Mismatched bracket {0}'.format(c))
            exit()
        elif opn.index(prev) != cls.index(c):
            print('Mismatched bracket {0} instead of {1} found'
                  .format(c, cls[opn.index(prev)]))
            exit()


print('Parens OK')
