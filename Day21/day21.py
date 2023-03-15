def make_tuples(liste1: list, liste2: list):
    if len(liste1) == len(liste2):
        zipped = zip(liste1, liste2)
        return print(list(zipped))
    else:
        return print("both list should have same length")


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
make_tuples(list1, list2)
