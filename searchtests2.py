# We import the librarys and modules that wee need:
#from ast import Pass
import unittest
# import jmespath
# from jmespath import search
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


# Todo se ejecutara en una pestaña diferente:
class SearchTests(unittest.TestCase):
    
    def setUp(self):
        # Preparacion del Driver:
        chrome = Service(r'C:\Users\Flavio Carrola\Desktop\My learning\chromedriver_win32\chromedriver.exe')
        self.driver = webdriver.Chrome(service=chrome)
        driver = self.driver
        # Para ir al sitio:
        # Maximize la ventana, de acuerdo 
        # a los eleento responsivos que cambian de
        # ubicación u orden dependiendo del tamaño de la vista:
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    # Busquedas de forma automatizadas:
    def test_search_tee(self):
        '''
        Identifica el boton de busqueda, limpia la entra si 
        es que contiene texto, ingresa unas teclas (input) y 
        lo manda para realizar la busqueda'''
        driver = self.driver
        # Campo de busqueda:
        search_field =  driver.find_element(By.NAME, 'q')
        # Limpieza en caso de que contenga un texto:
        # search_field.clear()

        # Manda teclas como un input():
        search_field.send_keys('tee')
        # Enviar Datos:
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        # Campo de busqueda:
        search_field = driver.find_element(By.NAME, 'q')

        # Ingresa texto y entrega al navegador:
        search_field.send_keys('salt shaker')
        search_field.submit()

        # Assert
        # xpath = '//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a'
        products = driver.find_elements(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        
        # Identifica si la cantidad de productos es uno o no:
        self.assertEqual(1, len(products))

    def tearDown(self):
        # Cerrar todo el proceso.
        self.driver.quit()
    

if __name__ == "__main__":
    unittest.main(verbosity = 2)