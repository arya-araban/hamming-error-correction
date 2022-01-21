def split(a, n):
    # this functions splits array "a" into equal chunks "n" (returns 2d array)
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))
