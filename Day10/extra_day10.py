def convert_number(listed: list):
    number = []
    for num in listed:
        number.append("{:,}".format(num))
    return print(number)


listed_num = [1000000, 2356989, 2354672, 9878098]
convert_number(listed_num)