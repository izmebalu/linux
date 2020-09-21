import unittest
from testcase1 import *
from testcase2 import *

tc1=unittest.TestLoader().loadTestsFromTestCase(Test1)
tc2=unittest.TestLoader().loadTestsFromTestCase(Test2)

ts=unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner().run(ts)