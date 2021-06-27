def minmax(data):
    _max = 0
    _min = 99999
    for i in data:
        if i < _min:
            _min = i
        if i > _max:
            _max = i
    return _min, _max


_data = {3, 7, 79, 2, 246, 287, 13, 9, 3, 99, 4, 138, 53, 84, 4, 88}
print(minmax(_data))
