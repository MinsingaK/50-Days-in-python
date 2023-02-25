def your_vat():
    while True:
        try:
            price = int(input("Enter the price of your item : "))
            vat = int(input("Enter the VAT of your item : "))
            if price < 0 or vat < 0:
                print("entries must be positives")
            elif vat > 90:
                print("The VAT can't be more than 90")
            else:    
                new_price = price + (price*vat)/100
                return print(f"the new price of your item is {new_price}.")
        except ValueError:
            print("Both price and VAT must be integers")


your_vat()