def capitalize(string: str):
    upp = []
    for i, elt in enumerate(string.split()):
        if elt[0].islower():
            upp.append(elt.capitalize())
        else:
            upp.append(elt)
    upp = ' '.join(upp)
    return print(upp)


capitalize('i like learning')