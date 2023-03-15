import string


def upper_case(chaine: str):
    new_list = []
    for elt in chaine.split():
        for j in elt:
            if j in string.ascii_uppercase:
                new_list.append("".join(elt[::-1]))
    return print(new_list)


str1 = 'leArning is hard, bUt if You appLy youRself ' \
'you can achieVe success'
upper_case(str1)