# Rescribir una serie de métodos para un objeto, que funcionarán para
# ejecutar las pruebas.
NOTA = ''' NOTA IMPORTANTE PAPIRRIN: 
            Estas son todas la pruebas que se instaciaran en '''

# Cargamos las bibliotecas:
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# CLase de prueba:
class GooglePage(object):
    def __init__(self, driver):
        self._driver = driver
        self._url = 'https://google.com'
        self.search_locator = 'q'

        # Propiedades(Se usarán como pruebas):
        @property
        def is_loaded(self):
            WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
            return True

        # Identificar el sitio de busqueda:
        @property
        def keyword(self):
            input_field = self._driver.find_element(By.NAME, 'q')
            return input_field.get_attribute('value')

        # Método con los cuales trabajra el page object:
        def open(self):
            self._driver.get_url(self.url)
        
        def type_search(self, keyword):
            input_field = self._driver.find_element(By.NAME, 'q')
            input_field.send_keys(keyword)

        def click_submit(self):
            input_field = self._driver.find_element(By.NAME, 'q')
            input_field.submit()

        def search(self, keyword):
            self.type_search(keyword)
            self.click_submit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)   