POM = '''
    Page Object Model (POM):
    Es un Patron de Diseño en Testing,
    En lugar de tener las pruebas en un solo archivo, tiene las pruebas 
    en diferentes archivos a las cuales se les llamarán 'Pages'.

    Beneficios:
    * Crea un alto nivel de astracción para minimizar cambios en las pruebas si
      los desarroladores modifican el sitio.
    * Crea un código reutilizable que se puede utiliar en multiples pruebas.
    * Las pruebas son más legibles, flexiblex y vigentes.

    
    '''
# Cargamos las bibliotecas:
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Importamos la clase de las pruebas desde tes_google.py:
# Video
# from google_page import GooglePage
from test_google import GooglePage

# CLASE DE PRUEBA:
class GoogleTest(unittest.TestCase):
    '''
    En esta ocasión se utilizara la sintaxis de @decorador @classmethod:
    para lo cual tendremos que cambiar todos los self. por cls.
    '''
    @classmethod
    def setUp(cls):
        # Preparacion del Driver:
        chrome = Service(r'C:\Users\Flavio Carrola\Desktop\My learning\chromedriver_win32\chromedriver.exe')
        cls.driver = webdriver.Chrome(service=chrome)
        driver = cls.driver

        driver.get('http://demo-store.seleniumacademy.com/')
        driver.find_element(By.LINK_TEXT, 'Sortable Data Tables').click()
    
    # CASO DE PRUEBA:
    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Platzi')

        self.assertEqual('Platzi', google.keyword)


    @classmethod
    def tearDownClass(cls):
        # Cerrar todo el proceso.
        cls.driver.close()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)    