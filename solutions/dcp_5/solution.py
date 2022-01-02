def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


def car(f):
    return f(lambda a, b: a)


def cdr(f):
    return f(lambda a, b: b)


assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4
