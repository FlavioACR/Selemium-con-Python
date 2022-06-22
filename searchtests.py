# We import the librarys and modules that wee need:
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

# Si class methos para hacerlo todo en una pestañra


class HolaMundo(unittest.TestCase):
    
    def setUp(self):
        # Preparacion del Driver:
        chrome = Service(r"C:\Users\Flavio Carrola\Desktop\My learning\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome(service=chrome)
        driver = self.driver
        # Para ir al sitio:
        driver.get('http://demo-store.seleniumacademy.com/')
        # Maximize la ventana, de acuerdo 
        # a los eleento responsivos que cambian de
        # ubicación u orden dependiendo del tamaño de la vista.
        driver.maximize_window()
        driver.implicitly_wait(14)

    def test_search_texte_field(self):
        # Define como se realizará la busqueda del elemento:
        search_field = self.driver.find_element_by_name("q")    

    def test_search_texte_field_by_class_name(self):
        # Define como se realizará la busqueda del elemento:
        search_field = self.driver.find_element_by_class_name("input-text required-entry")    

    def tearDown(self):
        # Cerrar todo el proceso.
        self.driver.quit()
    

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="report", report_name="hello_word_report"))
