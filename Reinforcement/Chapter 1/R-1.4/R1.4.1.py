def sum_of_squares(n):
    _sum = 0
    if n > 0:
        for i in range(n):
            _sum = _sum + i ** 2

    return _sum


print(sum_of_squares(2))
