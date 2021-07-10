_list=[1]

try:
    _list[3]=1
except IndexError:
    print("index out of bound")