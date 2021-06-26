def is_multiple(n, m):
    for i in range(0, n):
        if m * i == n:
            return True
    return True if m == 1 else False


print(is_multiple(6, 0))
