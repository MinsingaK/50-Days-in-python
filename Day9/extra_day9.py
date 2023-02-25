def zero_last(listed: list):
    if 0 not in listed:
        listed.sort()
    else:
        for i in listed:
            if i == 0:
                listed.remove(i)
                listed.append(0)
    return print(listed)


listed1 = [1, 4, 6, 0, 7, 0, 9]
listed2 = [2, 1, 4, 7, 6]

zero_last(listed1)
zero_last(listed2)
