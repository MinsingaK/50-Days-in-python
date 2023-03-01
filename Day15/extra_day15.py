def your_age(dico: dict):
    name = input("What's your name ? ").lower()
    if name in dico.keys():
        print(f"Hi {name}, you are {dico.get(name)} years old.")
    else:
        while name not in dico.keys():
            print("Your name is not in the database.\n")
            age_user = int(input("Enter your age : "))
            dico.update({name: age_user})
            print(f"Hi {name}, you are {dico.get(name)} years old.")
            return print(dico)


names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}
your_age(names_age)
