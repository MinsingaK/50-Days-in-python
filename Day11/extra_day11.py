def swap_values(liste:list):
    val = liste[0]
    liste[0] = liste[-1]
    liste[-1] = val
    return print(liste)

liste_num = [2, 4,67, 7]
swap_values(liste_num)