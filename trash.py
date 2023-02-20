while True:
    age = input("entrer votre age : ")
    try:
        age = int(age)
    except ValueError:
        print("L'age entre n'est pas bon")