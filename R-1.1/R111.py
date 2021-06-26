def is_multiple(n, m):
    if m > 0:
        return n % m == 0  # RETURNS Ture if multiples of i of m is equal to n
    return False


print(is_multiple(6, 0))
