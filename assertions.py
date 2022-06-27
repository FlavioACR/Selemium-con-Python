# Preparando Assertions y test suites:

# Assertions: Método de Verificación del test para fallar o continuar.
# Test Suites: Colección de pruebas en un solo archivo.

# Librerias y modulos:
# MIAS:
# import unittest
# from pyunitreport import HTMLTestRunner
# from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# # Sirve como una exepción para validar algun dato.
# from selenium.common.exceptions import NoSuchElementException
# # Ayuda a llamar a las exepciones que se buscan llamar.
# from selenium.webdriver.common.by import By

# OTHER
import unittest
from selenium import webdriver
#sirve como excepción para los assertions cuando queremos
#validar la presencia de un elemento
from selenium.common.exceptions import NoSuchElementException
#ayuda a llamar a las excepciones que queremos validar
from selenium.webdriver.common.by import By


class AssertionsTest(unittest.TestCase):

    def setUp(self):
        chrome = Service(r'C:\Users\Flavio Carrola\Desktop\My learning\chromedriver_win32\chromedriver.exe')
        self.driver = webdriver.Chrome(service=chrome)
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_field(self):
        # Aplicamos funcion is element.
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    # Validar opción para elegir lenguajes por medio del id:
    def test_language(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))  
    
    def tearDown(self):
        self.driver.quit()

    # Se define función para usarse arriba, permite encontrar los elementos.
    def is_element_present(self, how, what):
        '''
        Función de utilidad para identificar cuando un elemento esta presente:

        how = Indica el tipo de selector
        what = El valor del selector.

        '''
        try:
            # Buscar atravez del driver el elemento,
            # con los parametros, indicados:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True


if __name__ == '__main__':
    unittest.main(verbosity = 2)


    