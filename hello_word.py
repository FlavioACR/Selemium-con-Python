import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TesCase):

    def setUp(self):
        return super().setUp()

    def test_hello_word(self):
        pass

    def tearDown(self):
        retunr super().tearDown()

if __name__ == "__main__":
    unittest.main(verbosity = 2,)