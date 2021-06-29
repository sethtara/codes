def odd_product(seq):
    list2 = []
    l = len(seq) - 1
    for i in range(l):
        if (seq[i] * seq[i + 1]) % 2 != 0:
            list2.append([seq[i], seq[i + 1]])
        else:
            continue
    return list2


list1 = [1, 2, 5, 7, 4, 11, 7]
print(odd_product(list1))
