from checkout import Checkout


checkout = Checkout()

customer_name = input("What is the customer's name? ")

while True:

    product = input("What did the user buy? ")

    quantity = int(input("How many pieces? "))

    price = float(input("How much per unit? "))

    checkout.add_product(product,quantity, price)

    add_more = input("Add more items? ")

    if add_more.lower() != "yes":
        break


cashier_name = input("What is cashier's name? ")

discount = float(input("How much discount will he get? "))


print()
print("========================================")
print("        SEMICOLON STORE CHECKOUT")
print("========================================")

print()
print(f"Customer: {customer_name}")
print()

print(
    f"{'PRODUCT':<15}"
    f"{'QTY':<8}"
    f"{'UNIT PRICE':<15}"
    f"{'TOTAL':<15}"
)

print("----------------------------------------")


for index in range(len(checkout.products)):

    item_total = checkout.calculate_item_total(index)

    print(
        f"{checkout.products[index]:<15}"
        f"{checkout.quantities[index]:<8}"
        f"{checkout.prices[index]:<15.2f}"
        f"{item_total:<15.2f}"
    )


print("----------------------------------------")


subtotal = checkout.calculate_subtotal()
discount_amount = checkout.calculate_discount(discount)
after_discount = checkout.calculate_amount_after_discount(discount)
vat = checkout.calculate_vat(discount)
total = checkout.calculate_total(discount)


print(f"Subtotal:                 ₦{subtotal:.2f}")
print(f"Discount ({discount}%):           ₦{discount_amount:.2f}")
print(f"Amount after discount:    ₦{after_discount:.2f}")
print(f"VAT (7.5%):               ₦{vat:.2f}")
print(f"TOTAL:                    ₦{total:.2f}")

print()
print(f"Cashier: {cashier_name}")

print()

amount_paid = float(input("How much did the customer give you? "))

balance = checkout.calculate_balance(discount, amount_paid)

print(f"Amount Paid:              ₦{amount_paid:.2f}")
print(f"Balance:                  ₦{balance:.2f}")
