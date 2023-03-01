def sum_list(nested_list: list):
    som = 0
    for item in nested_list:
        for j in item:
            som = som + j
    return print(f"Somme of elements of the nested list is {som} .")


my_liste = [[2, 4, 5, 6], [2, 3, 5, 6]]
sum_list(my_liste)