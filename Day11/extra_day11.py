def swap_values(listed: list):
    val = listed[0]
    listed[0] = listed[-1]
    listed[-1] = val
    return print(listed)


listed_num = [2, 4, 67, 7]
swap_values(listed_num)
