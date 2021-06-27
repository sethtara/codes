def is_even(k):
    even = False
    for i in range(k + 1):
        if even:
            even = False
        else:
            even = True
    return even


print(is_even(2))