def pnorm(n, p=2):
    sums = 0
    for i in n:
        sums += i ** p

    return sums ** (1 / p)


ln = [1, 2, 3, 4, 5]
print(pnorm(ln))

