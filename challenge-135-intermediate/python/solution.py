from re import sub


class NoOpToken(object):
    def __repr__(self):
        return self.__class__.__name__

    def __str__(self):
        return ''

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

    def __repr__(self):
        return '{0}({1})'.format(self.__class__.__name__, self._name)


class BooleanOperatorToken(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def negate(self):
        if self._name == 'NOT':
            return NoOpToken()
        self._name = 'OR' if self._name == 'AND' else 'AND'
        return self

    def __str__(self):
        return self.name

    def __repr__(self):
        return '{0}({1})'.format(self.__class__.__name__, self._name)


class SubExpression(object):
    def __init__(self, tokens):
        self._tokens = tokens

    def add_token(self, tok):
        self._tokens.append(tok)

    def negate(self):
        self._tokens = [tok.negate() for tok in self._tokens]
        return self

    def flatten(self):
        flattened = []
        for tok in self._tokens:
            flattened.extend(tok.flatten() if hasattr(tok, 'flatten') else [tok])
        return flattened

    def __repr__(self):
        return '{0}({1})'.format(self.__class__.__name__, self._tokens)


def parse(items):
    tokens = []
    sub_expr_end_index = -1
    for i, tok in enumerate(items):
        i += 1
        if i <= sub_expr_end_index:
            continue
        if tok not in ('AND', 'OR', 'NOT', '(', ')'):
            tokens.append(LiteralToken(tok))
        elif tok in ('AND', 'OR', 'NOT'):
            tokens.append(BooleanOperatorToken(tok))
        elif tok == '(':
            sub_expr_end_index = i + items[i:].index(')')
            toks = parse(items[i:sub_expr_end_index])
            tokens.append(SubExpression(toks))
    return tokens


def negate(tr):
    negated = []
    skip_next = False
    for ti in tr:
        if skip_next:
            negated.append(ti)
            skip_next = False
            continue
        nti = ti.negate()
        if isinstance(nti, NoOpToken):
            skip_next = True
            continue
        negated.append(nti)

    return negated


if __name__ == '__main__':
    code = 'a AND b'
    print(code)
    tree = parse(sub(r'\s{2,}', ' ', sub(r'(\(|\))', r' \1 ', code)).strip().split(' '))
    print('parsed tree:', tree)
    negated_tree = negate(tree)
    print('negated tree:', negated_tree)
    flat_tree = []
    for item in negated_tree:
        flat_tree.extend(item.flatten() if hasattr(item, 'flatten') else [item])
    print('flat tree:', flat_tree)
    print('After DeMorgan:', ' '.join(map(str, flat_tree)))
