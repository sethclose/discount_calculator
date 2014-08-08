import unittest

from discount_calculator import calculate_discount

class InvoiceCalculatorTests(unittest.TestCase):

    def testDividedFairly(self):
        price = calculate_discount(100, 10, 30)
        #import pdb; pdb.set_trace()
        self.assertEqual(price, 60)

    def testTooBigDiscount(self):
        with self.assertRaises(ValueError):
            #import pdb; pdb.set_trace()
            price = calculate_discount(100, 10, 91)

if __name__ == "__main__":
    unittest.main()