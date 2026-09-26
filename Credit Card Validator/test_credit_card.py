import unittest

from credit_card_functions import CreditCardFunctions

class CreditCardTest(unittest.TestCase):
    
    def setUp(self):
        
        self.credit_card_functions = CreditCardFunctions()
        
    
    def test_that_card_length_is_valid(self):

        card_number = "4388576018410707"

        actual = self.credit_card_functions.is_valid_length(card_number)

        self.assertEqual(True, actual)


    def test_that_card_length_is_invalid_when_less_than_13(self):

        card_number = "43885760184"

        actual = self.credit_card_functions.is_valid_length(card_number)

        self.assertEqual(False, actual)


    def test_that_card_length_is_invalid_when_more_than_16(self):

        card_number = "43885760184107078"

        actual = self.credit_card_functions.is_valid_length(card_number)

        self.assertEqual(False, actual)
        

    def test_that_visa_card_is_detected(self):

        card_number = "4388576018410707"

        actual = self.credit_card_functions.get_card_type(card_number)

        self.assertEqual("Visa", actual)


    def test_that_mastercard_is_detected(self):

        card_number = "5399831619690403"

        actual = self.credit_card_functions.get_card_type(card_number)

        self.assertEqual("MasterCard", actual)


    def test_that_american_express_is_detected(self):

        card_number = "371449635398431"

        actual = self.credit_card_functions.get_card_type(card_number)

        self.assertEqual("American Express", actual)


    def test_that_discover_card_is_detected(self):

        card_number = "6011111111111117"

        actual = self.credit_card_functions.get_card_type(card_number)

        self.assertEqual("Discover", actual)


    def test_that_valid_card_passes_luhn_check(self):

        card_number = "4388576018410707"

        actual = self.credit_card_functions.is_valid_card_number(card_number)

        self.assertEqual(True, actual)


    def test_that_invalid_card_fails_luhn_check(self):

        card_number = "4388576018402626"

        actual = self.credit_card_functions.is_valid_card_number(card_number)

        self.assertEqual(False, actual)


    def test_that_sample_mastercard_is_invalid(self):

        card_number = "5399831619690413"

        actual = self.credit_card_functions.is_valid_card_number(card_number)

        self.assertEqual(False, actual)


