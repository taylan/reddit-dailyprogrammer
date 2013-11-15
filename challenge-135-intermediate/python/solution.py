from re import sub


class LiteralToken(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def negate(self):
        return SubExpression([BooleanOperatorToken('NOT'), self])

    def __str__(self):
        return self.name


class BooleanOperatorToken(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def negate(self):
        if self._name == 'NOT':
            return self
        self._name = 'OR' if self._name == 'AND' else 'AND'
        return self

    def __str__(self):
        return self.name


class SubExpression(object):
    def __init__(self, tokens=[]):
        self._tokens = tokens

    def add_token(self, tok):
        self._tokens.append(tok)

    def negate(self):
        self._tokens = [t.negate() for t in self._tokens]
        return self

    def simplify(self):
        newtoks = []
        for t in self._tokens:
            if isinstance(t, SubExpression):
                newtoks.extend([v for v in t.simplify() if str(v) != ''])
            elif str(t):
                newtoks.append(t)
        self._tokens = newtoks
        return self._tokens


def parse(items, level=0):
    tokens = []
    sub_expr_end_index = -1
    for i, t in enumerate(items):
        i += 1
        if i <= sub_expr_end_index:
            continue
        if t not in ('AND', 'OR', 'NOT', '(', ')'):
            tokens.append(LiteralToken(t))
        elif t in ('AND', 'OR', 'NOT'):
            tokens.append(BooleanOperatorToken(t))
        elif t == '(':
            level += 1
            sub_expr_end_index = i + items[i:].index(')')
            toks, lvl = parse(items[i:sub_expr_end_index], level)
            tokens.append(SubExpression(toks))
    return tokens, level


def simplify(tree):
    flat_tree = []
    for t in tree:
        if hasattr(t, 'simplify'):
            t.simplify()
    for t in tree:
        flat_tree.extend(t._tokens if hasattr(t, '_tokens') else [t])
    simplified = []
    skip_next = False
    for i, t in enumerate(flat_tree):
        if skip_next or str(t) == '':
            skip_next = False
            continue
        if hasattr(t, 'simplify'):
            t.simplify()
        if str(t) == 'NOT' and len(flat_tree) > i and str(flat_tree[i+1]) == 'NOT':
            skip_next = True
            continue
        simplified.append(str(t))
    return [s for s in simplified if s]


if __name__ == '__main__':
    code = 'NOT (a OR b AND C) OR NOT(a AND NOT b)'
    tree, level = parse(sub(r'\s{2,}', ' ', sub(r'(\(|\))', r' \1 ', code)).strip().split(' '))
    negated_tree = [t.negate() for t in tree]
    print(' '.join([str(s) for s in (simplify(negated_tree))]))

