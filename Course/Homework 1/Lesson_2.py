def cube_root(n):
    res = 1
    while not guess_enough(res, n):
        res = improve(res, n)
    return res


def guess_enough(x, y):
    if abs(x**2 - y) < 0.0001:
        return True
    else:
        return False


def improve(m, n):
    return (m/(n**2) + 2 * m) / 3


print(cube_root(27))  # output is equal to 3
