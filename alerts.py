# MANEJAR ALERT & POP-UP:

# Librerías:
from lib2to3.pgen2 import driver
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# Modulo para manejar dropdown:
from selenium.webdriver.support.ui import Select

# CLASE DE PRUEBA:
class CompareProducts(unittest.TestCase):
    '''Clase que automatiza la prueba  de comparar preción de una busqueda determinada'''
    
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
    
    def test_compare_product_removal_alert(self):
        '''Definición de la función pendiente: XX XXX XX'''
        driver = self.driver
        
        # Identificaremos la barra de busqueda y como buena practica eliminamos el texto
        # dentro de la barra si es que existe:
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()

        # Escribiremos un input en la barra de busqueda y lo mandaremos con submit:
        search_field.send_keys('tee')
        search_field.submit()

        # Buscamos la ubicación del elemento para agregar a la lista de comparación
        # y hacemos click en el elemento:
        driver.find_element(By.CLASS_NAME, 'link-compare').click()
            # Buscaremos el elemento de 'Clear all', mediante el texto
        # y hacemos click en elemento:
        driver.find_element(By.LINK_TEXT, 'Clear All').click()

        # ALERTA
        # Para interactuar con el alert, haremos un cambio asignado dentro de una variable
        # con lo cual el cursor dentro del navegador se centrará en el 'alert' :
        alert = driver.switch_to.alert
        # Extraeremos el texto de la alerta y lo almacenaremos dentro de un variable:
        alert_text = alert.text
        print('ALERTA !!!:', '\n',alert_text)
        # Validamos por medio de un assert que el texto de la alerta es el texto correcto:
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)
        # Aceptamos o valizdamos el alert:
        alert.accept()  
        
    def tearDown(self):
        # Cerrar todo el proceso.
        self.driver.implicitly_wait(4)
        self.driver.quit()
    

if __name__ == "__main__":
    unittest.main(verbosity = 2)
