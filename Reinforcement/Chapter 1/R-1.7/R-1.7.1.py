def sum_of_odd_squares(n):
    return sum([i ** 2 for i in range(n) if i % 2 != 0])


print(sum_of_odd_squares(4))
