def count_douts(chaine: str):
    count = 0
    for j in chaine:
        if j == '.' in chaine:
            count += 1
    return print(f"there are {count} dots in {chaine}")


ch1 = 'h.e.l.p.'
ch2 = 'he.l.p.'
count_douts(ch2)
count_douts(ch1)
