
# Librerías:
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# Agrega pausas pero aumenta el tiempo de la prueba:
from time import sleep

# CLASE DE PRUEBA:
class NavigationTest(unittest.TestCase):
    '''Clase que automatiza la navegación y busqueda dentro del navegador'''
    
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
        driver.get('https://google.com/')
    
    # CASO DE PRUEBA:
    def test_browser_navigation(self):
        '''Navegación en navegador automatizada'''
        driver = self.driver
        # Ubicamos la barra de busqueda:
        search_field = driver.find_element(By.NAME, 'q')
        # Eliminamos texto dentro de la barra si es que existe:
        search_field.clear()
        # Escribimos y mandamos una busqueda:
        search_field.send_keys('platzi')
        search_field.submit()

        # Vamor a retroceder, avanzar y refrescar una pagina en ese orden:
        driver.back()
        sleep(2)
        driver.forward()
        sleep(3)
        driver.refresh()
        sleep(4)
        
        
    def tearDown(self):
        # Cerrar todo el proceso.
        self.driver.implicitly_wait(8)
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)
