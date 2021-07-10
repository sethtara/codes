_list = []
n = 1
while n == 1:
    try:
        a = input("something")
        _list.append(a)
    except EOFError:
        for i in range(len(_list) - 1, -1, -1):
            print(_list[i])
            n = 0
