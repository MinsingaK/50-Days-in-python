def even_or_average():
    print("Enter five numbers.")
    liste_num = []
    even_num = []
    while True:
        try:
            num = int(input())
            liste_num.append(num)
            if num % 2 == 0:
                even_num.append(num)
            if len(liste_num) == 5:
                break
        except ValueError:
            print("Enter a good number!")
    if len(even_num) > 0:
        large = max(even_num)
        return print(f"The max number of the event list is {large}.")
    else:
        avg = sum(liste_num) / len(liste_num)
        return print(f"The average of numbers of the list without even numbers is {avg:.2f}")


print(even_or_average())

