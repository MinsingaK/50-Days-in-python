def zero_last(liste:list):
    if 0 not in liste:
        liste.sort()
    else :
        for i in liste:
            if i == 0:
                liste.remove(i)
                liste.append(0)
    return print(liste)

liste1 = [1, 4, 6, 0, 7,0,9]
liste2 = [2, 1, 4, 7, 6]

zero_last(liste1)
zero_last(liste2)
