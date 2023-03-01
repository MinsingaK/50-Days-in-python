def same_in_reverse(chaine: str):
    #chaine[::-1] permet de lire la chaine de caractère à l'envers
    if chaine == chaine[::-1]:
        return True
    else:
        return False

print(same_in_reverse('mama'))