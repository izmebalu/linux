import unittest
class Test2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This is setup class")
    def setUp(self):
        print("This is setup method")
    def test_3(self):
        print("This is test3 method")
    def tearDown(self):
        print("This is teardown method")
    @classmethod
    def tearDownClass(cls):
        print("This is teardown class")


if __name__ == '__main__':
    unittest
