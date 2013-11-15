from tokenize import tokenize
from io import BytesIO


class LiteralToken(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

class BooleanOperatorToken(object):
    def __init__(self, name):
        self._name = name

    def reverse(self):
        return 'OR' if self._name == 'AND' else 'AND'

with open('input.txt') as f:
    for l in f.readlines():
        for toknum, tokval, _, _, _  in tokenize(BytesIO(l.encode('utf-8')).readline):
            print(toknum, tokval)

        #print(tokenize(BytesIO(l.encode('utf-8')).readline))