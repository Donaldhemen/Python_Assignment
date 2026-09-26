import credit_card_functions

card_number = input("Hello, kindly enter Card details to verify: ")

card_type = credit_card_functions.get_card_type(card_number)

validity = credit_card_functions.is_valid_card_number(card_number)

print()
print("**Credit Card Type:", card_type)
print("**Credit Card Number:", card_number)
print("**Credit Card Digit Length:", len(card_number))

if validity:
    print("**Credit Card Validity Status: Valid")
else:
    print("**Credit Card Validity Status: Invalid")
