def my_discount():
    price = float(input("Enter the product's price : "))
    disc = int(input("Enter the discount : "))
    new_price = price - (price*disc)/100
    return print(f"The new price after discount is {new_price}€")

my_discount()