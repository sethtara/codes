def count_vowels(_string):
    count = 0
    for i in _string:
        if i.lower() in {'a', 'e', 'i', 'o', 'u'}:
            count += 1
    return count


print(count_vowels('hOw are you'))
