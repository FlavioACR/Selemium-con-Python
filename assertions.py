import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
# Sirve como una exepción para validar algun dato.
from selenium.webdriver.common.by import By
# Ayuda a llamar a las exepciones que se buscan llamar.

class AssertionsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= '../chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))
    
    # Me quede en el minuto 5:35

    def tearDown(self):
        self.driver.quit()

    # Permite encontrar los elementos.
    def is_element_present(self, how, what):
        # Permite identificar cuando un elemento esta presente de acuerdo
        # a sus parametros.
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True


if __name__ == '__main__':
    unittest.main(verbosity = 2)


    