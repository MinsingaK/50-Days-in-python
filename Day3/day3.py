diction = {'Nkrumah': 'yes', 'Borel': 'yes', 'Jeff': 'no','Epalla':'yes','Arthur':'no','Donald':'yes'}

def register_check(dico:dict):
    count = 0
    for value in dico.values():
        if value == 'yes':
            count = count + 1
    return print("Number of students in school is ", count)


register_check(diction)
