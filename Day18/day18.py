def any_number(*n):
    som = sum(n)
    moyenne = som/len(n)
    return print(f"la moyenne des arguments est de {moyenne}")


any_number(2,5,7)