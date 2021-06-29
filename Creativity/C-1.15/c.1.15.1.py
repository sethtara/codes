def unique_(_list):
    l = len(_list)
    for i in range(l):
        for j in range(l):
            flag = 0
            if _list[i] == _list[j]:
                flag += 1
                if flag == 2:
                    return False
    return True


list1 = [1, 2, 3, 4, 6, 9, 7, 8]
print(unique_(list1))
