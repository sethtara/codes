def num_reverse(_list):
    temp = []
    l = len(_list) - 1
    for i in range(l, -1, -1):
        temp.append(_list[i])
    return temp


list1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(num_reverse(list1))
