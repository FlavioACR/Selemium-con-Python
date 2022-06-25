# We import the librarys and modules that wee need:
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

# Realizado con class method para ejecutar el testing en una sola pestaña del navegador:
class HolaMundo(unittest.TestCase):
    '''Esta clase se divide en 3 partes;
    
    Para correr las preubas y el codigo en una sola pestaña se agrego
    el class method al nombre de la función se agregal el Class 
    y se cambiaron los self, por cls.
    Pero solo en la función setUps y en la función tearDown.
    
    '''
    @classmethod
    def setUpClass(cls):
        # Preparar el entorno antes de la prueba, que es lo que se va a hacer:
        # Ruta del driver:
        chrome = Service(r"C:\Users\Flavio Carrola\Desktop\My learning\chromedriver_win32\chromedriver.exe")
        # Ruta del driver en variable:
        # Optimizamor la variable que controla el driver, para no repetir lo anterior constantemente:
        cls.driver = webdriver.Chrome(service=chrome)
        # Le decimos al driver que esperde determinado tiempo antes de hacer otra acción:
        WebDriverWait(cls.driver, 15)
        
    def test_hola(self):
        # Caso de prueba serie de acciones para automatizar:
        # Declaramos nuevamente la variable driver
        self.driver.get("https://www.linkedin.com/feed/")
    
    def test_wiki(self):
        # Caso de prueba serie de acciones para automatizar:
        # Declaramos nuevamente la variable driver
        self.driver.get("https://www.wikipedia.org")

    @classmethod
    def tearDownClass(cls):
        # Acciones para finalizar la prueba:    
        # Cierra ventana cuando la prueba finaliza:
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="report", report_name="hello_word_report"))
