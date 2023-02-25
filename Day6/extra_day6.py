# to access a list to the bottom, use the minus sign and the index for example :liste[-i]

def zeroed(liste:list) -> list:
    liste[0] = 0
    liste[-1] = 0
    return print(liste)


number = [1, 3, 5, 7, 5, 33]
zeroed(number)


