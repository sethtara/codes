def sum_of_odd_squares(n):
    _sum = 0
    if n > 0:
        for i in range(n):
            if i % 2 == 0:
                continue
            else:
                _sum += i ** 2
    return _sum


print(sum_of_odd_squares(3))
