def convert_number(liste:list):
    number = []
    for num in liste:
        number.append("{:,}".format(num))
    return print(number)

liste_num = [1000000, 2356989, 2354672, 9878098]
convert_number(liste_num)