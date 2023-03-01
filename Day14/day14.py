#My solution
def flat_list(liste: list):
    my_list = []
    for i in liste[0]:
        my_list.append(i)
    return print(my_list)

#Book's correction
def flat_list(liste: list):
    my_list = []
    for items in liste:
        for i in items:
            my_list.append(i)
    return print(my_list)


liste = [[2,4,5,6]]
flat_list(liste)

liste = [[2,4,5,6]]
flat_list(liste)