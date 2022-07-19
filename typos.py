# Librerías:
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# CLASE DE PRUEBA:
class Typos(unittest.TestCase):
    '''Automatización de la examinación del texto de un sitio web'''
    def setUp(self):
        # Preparacion del Driver:
        chrome = Service(r'C:\Users\Flavio Carrola\Desktop\My learning\chromedriver_win32\chromedriver.exe')
        self.driver = webdriver.Chrome(service=chrome)
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Typos').click()
            
    #  CASOS DE PRUEBA:
    def test_find_typo(self):
        driver = self.driver

        # Creamos una variable donde buscaremos el elemento de texto que deseamos verificar:
        paragraph_to_check = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')
        # Creamos una nueva variabld donde guardaremos unicamente el texto del elemento:
        text_to_chek = paragraph_to_check.text
        print(text_to_chek)

        # Creamos las siguientes variables de control:
        
        # Contará el numero de veces hasta encontrar el texto correcto:
        tries = 1
        # Indicará 'True' cuando el texto correco sea encontrado:
        found = False
        # Contiene el texto correcto:
        correct_text = "Sometimes you'll see a typo, other times you won't."


        # Cuando el texto tomado del parrafo es el equivocado:
        #       Si el texto a revisar es diferente al texto correcto:
        while text_to_chek != correct_text:
            # Actualizamos la variable donde buscaremos el elemento de texto que deseamos verificar:
            paragraph_to_check = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')
            # Actualizamos la variable donde guardaremos unicamente el texto del elemento:
            text_to_chek = paragraph_to_check.text
            # Cargamos una vez mas el navegador:
            driver.refresh()

        # Mientras que el valor de found sea falso:
        while not found:
            # Refrescaremos?
            if text_to_chek == correct_text:
                tries += 1
                driver.refresh()
                found = True

        # Assertion para continuar o no  la prueba:
        # Si la variable 'found' es igual a 'True';
        self.assertEqual(found, True)
        # Imprimimos cuanto le tomo a la prueba llegar a elemento correcto del texto:
        print(f'It took {tries} tries to find the typo')

    def tearDown(self):
        # Cerrar todo el proceso.
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)