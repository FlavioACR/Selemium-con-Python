import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    '''Esta clase se divide en 3 partes;'''

    def setUp(self):
        # Preparar el entorno antes de la prueba, que es lo que se va a hacer:

        # Indicaremos como procedera el driver:
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Flavio Carrola\Desktop\My learning\chromedriver_win32\chromedriver.exe')
        # Optimizamor la variable que controla el driver, para no repetir lo anterior constantemente
        driver = self.driver
        # Le decimos al driver que esperde determinado tiempoa antes de hacer otra acción:
        driver.implicity_wait(45)

    
    def test_hello_word(self):
        # Caso de prueba serie de acciones para automatizar:
        # Declaramos nuevamente la variable driver:
        driver = self.driver
        # Le damos la indicación de a donde ir "get":
        driver.get('https://platzi.com/home')

    def tearDown(self):
        # Acciones para finalizar la prueba:    
        # Cierra ventana cuando la prueba finaliza:
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello_world_report'))