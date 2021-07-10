def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k


fact = []
for i in factors(10):
    fact.append(i)

print(sorted(fact))
