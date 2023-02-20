def check_duplicates(liste:list):
    for i in liste:
        if liste.count(i) == 1:
            return print("No duplicates")
        else:
            return print(i)

fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']

check_duplicates(fruits)