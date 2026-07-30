def promotional_code(promo_code):

    if promo_code == "SAVE10" :
        discounted_price = original_price - (original_price * 0.1)
    
    elif promo_code == "HALFOFF" :
         discounted_price = original_price - (original_price * 0.5)
    
    else :
        discounted_price = original_price

    return discounted_price
item_name = input("Enter item name: ")
promo_code = input("Enter promotional code: ").upper()
original_price = float(input("Enter original price of item: "))
discount = promotional_code(promo_code)
print(item_name, " is ", discount)