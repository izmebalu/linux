import unittest
class Testdemo(unittest.TestCase):
    def setUp(self):
        print("setupmethod execution")
    def test_1(self):
        print("testmethod exection")
    def test_2(self):
        print("testmethod exection")
    def tearDown(self):
        print("teardown execution")


if __name__ == '__main__':
    unittest.main()
