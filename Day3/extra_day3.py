# tuple() method allows the transformation from a list to a tuple

def lower_case(liste:list):
    d = []
    for elt in sorted(liste, reverse=False):
        if elt != elt.capitalize():
            d.append(elt)
            tuples = tuple(d)
    return print(tuples)

names = ["kerry", "dickson", "John", "Mary","carol", "Rose", "adam"]
lower_case(names)