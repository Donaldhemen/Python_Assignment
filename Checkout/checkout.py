class Checkout:

    def __init__(self):
        self.products = []
        self.quantities = []
        self.prices = []

    def add_product(self, product, quantity, price):
        self.products.append(product)
        self.quantities.append(quantity)
        self.prices.append(price)

    def calculate_item_total(self, index):
        return self.quantities[index] * self.prices[index]

    def calculate_subtotal(self):
        subtotal = 0

        for index in range(len(self.products)):
            subtotal += self.calculate_item_total(index)

        return subtotal

    def calculate_discount(self, discount_percentage):
        subtotal = self.calculate_subtotal()

        return subtotal * discount_percentage / 100

    def calculate_amount_after_discount(self, discount_percentage):
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount(discount_percentage)

        return subtotal - discount

    def calculate_vat(self, discount_percentage):
        amount_after_discount = self.calculate_amount_after_discount(discount_percentage)

        return amount_after_discount * 7.5 / 100

    def calculate_total(self, discount_percentage):
        amount_after_discount = self.calculate_amount_after_discount(discount_percentage)

        vat = self.calculate_vat(discount_percentage)

        return amount_after_discount + vat

    def calculate_balance(self, discount_percentage, amount_paid):
        total = self.calculate_total(discount_percentage)

        return amount_paid - total
