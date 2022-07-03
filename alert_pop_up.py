# MANEJAR ALERT & POP-UP:

# Librerías:
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# Modulo para manejar dropdown:
from selenium.webdriver.support.ui import Select

# CLASE DE PRUEBA:
class LenguageOptions(unittest.TestCase):
    '''Clase que automatiza la prueba con un menu despegable tipo dropdown, en este caso el dropdown de selección de lenguaje. '''
    
    def setUp(self):
        # Preparacion del Driver:
        chrome = Service(r'C:\Users\Flavio Carrola\Desktop\My learning\chromedriver_win32\chromedriver.exe')
        self.driver = webdriver.Chrome(service=chrome)
        driver = self.driver

        # Para ir al sitio:
        # Maximize la ventana, de acuerdo a los elemetos responsivos que cambian de
        # ubicación u orden dependiendo del tamaño de la vista:
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')
    
        
    def tearDown(self):
        # Cerrar todo el proceso.
        self.driver.implicitly_wait(4)
        self.driver.quit()
    

if __name__ == "__main__":
    unittest.main(verbosity = 2)
