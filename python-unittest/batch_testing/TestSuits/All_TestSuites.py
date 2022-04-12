import unittest

from batch_testing.Package1.TC_LoginTest import LoginTest
from batch_testing.Package1.TC_SignUP import SignUPTest

from batch_testing.Package2.TC_PaymentTest import PaymentTest
from batch_testing.Package2.TC_PaymentReturns import PaymentReturnsTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignUPTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

TestSuite1 = unittest.TestSuite([tc1, tc2])
TestSuite2 = unittest.TestSuite([tc3, tc4])
TotalTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])

unittest.TextTestRunner().run(TotalTestSuite)