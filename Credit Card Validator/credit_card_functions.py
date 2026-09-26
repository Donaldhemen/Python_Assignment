
class CreditCardFunctions:

    def is_valid_length(self, card_number):

        return 13 <= len(card_number) <= 16
        
    def get_card_type(self, card_number):

        if card_number.startswith("4"):
            return "Visa"

        elif card_number.startswith("5"):
            return "MasterCard"

        elif card_number.startswith("37"):
            return "American Express"

        elif card_number.startswith("6"):
            return "Discover"

        else:
            return "Invalid"

    def double_digit(self, digit):

        result = digit * 2

        if result >= 10:
            result = (result // 10) + (result % 10)

        return result

    def get_luhn_sum(self, card_number):

        total = 0

        position = len(card_number) - 2

        while position >= 0:
            digit = int(card_number[position])

            total = total + self.double_digit(digit)

            position = position - 2

        position = len(card_number) - 1

        while position >= 0:
            digit = int(card_number[position])

            total = total + digit

            position = position - 2

        return total

    def is_valid_card_number(self, card_number):

        if not card_number.isdigit():
            return False

        if not self.is_valid_length(card_number):
            return False

        if self.get_card_type(card_number) == "Invalid":
            return False

        total = self.get_luhn_sum(card_number)

        return total % 10 == 0
