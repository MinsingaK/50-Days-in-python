def convert_add(liste:list):
    S = 0
    b = []
    for i in liste:
        b.append(int(i))
        S = S + int(i)
    return print("La Somme des termes est {} et la nouvelle liste est {}".format(S,b))

lis = ['1','5','9']
convert_add(lis)
