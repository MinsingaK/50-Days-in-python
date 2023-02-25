def prime_num():
    new = []
    num = int(input("Enter a number (an integer): "))
    for i in range(1, num+1):
        d = 0
        for j in range(1, i+1):
            if i % j == 0:
                d += 1
        if d == 2:
            new.append(i)
    return print(f"the list of prime numbers between 1 and {num} is {new}")


prime_num()
