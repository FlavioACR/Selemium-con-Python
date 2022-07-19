# Data Driven Testing (DDT):
# Metodología utilizada en el testing de sofware. Desarrolla pruebas en base al codigo existente
# para validar los escenarios pasan o no pasan.

# No confundir con el TDD (Testing Driven Development):
# Que desarrolla el codigo en base a pruebas para que pueda cumplirlas:


# Cargamos las bibliotecas:
import unittest
# Datos prestablecidos previamente, con los submodulos:
from ddt import ddt, data, unpack 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
#
# Decorador ??
@ddt    
# CLASE DE PRUEBA:
class Tables(unittest.TestCase):
    '''Automatización de la examinación del texto de un sitio web'''
    def setUp(self):
        # Preparacion del Driver:
        chrome = Service(r'C:\Users\Flavio Carrola\Desktop\My learning\chromedriver_win32\chromedriver.exe')
        self.driver = webdriver.Chrome(service=chrome)
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.find_element(By.LINK_TEXT, 'Sortable Data Tables').click()

    # Predefinimos el data con el cual estaremos haciendo los inputs:
    @data(('dress', 6), ('music', 5))
    # aplicamos el modulo para desempacar estos datos en el caso de prueba:
    @unpack

    #  CASOS DE PRUEBA:
    def test_shearch_ddt(self, search_value, expected_count):
        '''
        * search_value: Este parametro es el valor de busqueda.
        * expected_count: Este parametro de entrada es la cantidad de valores de busqueda esperados encontrar.

        '''
        driver = self.driver

        # Buscamos la barra de busqueda, por su nombre dentro del POM y lo guardamos dentro de la variable 
        # search_field.
        search_field = driver.find_element(By.NAME, 'q') 
        # Como buena practica limpiamos el texto de la barra si es que lo hay.
        search_field.clear()

        # Mandamos los datos utilizando el método .send_keys(), tomando como parametro
        # el parametro de la función 'search_value'.
        search_field.send_keys(search_value)
        # Mandamos los datos con el método submit.
        search_field.submit()

        # Identificar productos:
        products = driver.find_elements(By.XPATH, '//h2[@class="product_name"]/a')
        # Imprimir cuantos
        print(f'Found {len(products)} products')

        # Ciclo para ver los nombres de los productos:
        for product in products:
            print(product.text)

        # Comprobación con un assertion:
        self.assertEqual(expected_count, len(products))   
        

    def tearDown(self):
        # Cerrar todo el proceso.
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)