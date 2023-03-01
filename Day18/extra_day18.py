def add_reverse(liste1: list, liste2: list):
    liste3 = []
    if len(liste1) != len(liste2):
        print("the lists are not of equal lengths")
    else:
        for i in range(len(liste1)):
            liste3.append(liste1[i] + liste2[i])
            liste3.reverse()
        return print(liste3)


lis1 = [10, 12, 34,43]
lis2 = [12, 56, 78]
add_reverse(lis1,lis2)

