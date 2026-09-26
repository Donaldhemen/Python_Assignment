import unittest
from checkout import Checkout


class TestCheckout(unittest.TestCase):

    def setUp(self):
        self.checkout = Checkout()

        self.checkout.add_product("Parfait", 2, 2100)

        self.checkout.add_product("Rice", 2, 550)

    def test_that_product_can_be_added(self):

        self.assertEqual(len(self.checkout.products), 2)

    def test_that_item_total_can_be_calculated(self):

        self.assertEqual(self.checkout.calculate_item_total(0), 4200)

    def test_that_subtotal_can_be_calculated(self):

        self.assertEqual(self.checkout.calculate_subtotal(), 5300)

    def test_that_discount_can_be_calculated(self):

        self.assertEqual(self.checkout.calculate_discount(8), 424)

    def test_that_amount_after_discount_can_be_calculated(self):

        self.assertEqual(self.checkout.calculate_amount_after_discount(8), 4876)

    def test_that_vat_can_be_calculated(self):

        self.assertAlmostEqual(self.checkout.calculate_vat(8), 365.70, places=2)

    def test_that_total_can_be_calculated(self):

        self.assertAlmostEqual(self.checkout.calculate_total(8), 5241.70, places=2)

    def test_that_balance_can_be_calculated(self):

        self.assertAlmostEqual(self.checkout.calculate_balance(8, 6000), 758.30, places=2)

