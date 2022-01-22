from itertools import count


def split(a, n):
    # this functions splits array "a" into equal chunks "n" (returns 2d array)
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


def find_powers(num):
    pows = []
    # this function finds all powers of 2 that are below "num"
    for i in count(0):
        nm = 2 ** i
        if num < nm:
            return pows
        pows.append(nm)



