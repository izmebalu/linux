import unittest
class Test1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This is setup class")
    def setUp(self):
        print("This is setup method")
    def test_1(self):
        print("This is test1 method")
    def test_2(self):
        print("This is test2 method")
    def tearDown(self):
        print("This is teardown method")
    @classmethod
    def tearDownClass(cls):
        print("This is teardown class")


if __name__ == '__main__':
    unittest
