def only_floats(a,b):
    if type(a) == float and type(b) == float:
        return print("2")
    elif type(a) == float or type(b) == float:
        return print("1")
    elif type(a) != float and type(b) != float:
        return print("0")

only_floats(2.4,4.8)
    