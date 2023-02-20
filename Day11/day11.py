# here the sorted method is used to sort both string characters to
# allow simplified comparism

def equal_string(chaine1:str,chaine2:str):
    ch1 = sorted(chaine1)
    ch2 = sorted(chaine2)
    if ch1 == ch2:
        return True
    else :
        return False
print(equal_string("ananas","nanasa"))