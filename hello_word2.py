# This is only another type from hello_word.
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

class HolaMundo(unittest.TestCase):

    def setUp(self) -> None:
        chrome = Service(r"C:\Users\Flavio Carrola\Desktop\My learning\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome(service=chrome)
        WebDriverWait(self.driver, 10)

    def test_hola(self):
        self.driver.get("https://www.linkedin.com/feed/")

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output="report", report_name="holareport"))

