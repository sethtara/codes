def rem_punctn(_string):
    n_string=''
    for i in _string:
        if i not in '''.,<>:;?'"|''':
            n_string+=i
    return n_string


print(rem_punctn("hi how's your day."))
