import unittest

class PaymentTest(unittest.TestCase):

    def test_Paymentindollar(self):
        print("This is Payment in dollar Test")
        self.assertTrue(True)

    def test_Paymentinrupee(self):
        print("This is Payment in rupee Test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main

