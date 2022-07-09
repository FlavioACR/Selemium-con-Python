
# Librerías:
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

# CLASE DE PRUEBA:
class AddRemoveElements(unittest.TestCase):
    '''Caso de prueba de esperas automatizadas'''
    def setUp(self):
        # Preparacion del Driver:
        chrome = Service(r'C:\Users\Flavio Carrola\Desktop\My learning\chromedriver_win32\chromedriver.exe')
        self.driver = webdriver.Chrome(service=chrome)
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
            
    #  CASOS DE PRUeBA:
    def test_add_remove(self):
        driver = self.driver

        # Generamos una variable con entrada del usuario, cuantos elementos agregaremos y cuantos removeremos:
        elements_added = int(input('How many elements will you add ?: '))
        elements_removed = int(input('How many elements will you remove ?: '))
        total_elements = elements_added - elements_removed

        # Identificaremos el boton para agregar los elementos: POSIBLE CAMBIO AL XPATH:
        add_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')
        sleep(4)

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                delete_button = driver.find_element(By.XPATH, '//*[@id="elements"]/button')
                delete_button.click()
            except:
                print('You are trying to delect more elements that existent')

        if total_elements > 0:
            print(f"Ther are {total_elements} elements on screen")
        else:
            print('Ther are 0 elements on screen')
        
        sleep(3)


    def tearDown(self):
        # Cerrar todo el proceso.
        self.driver.implicitly_wait(8)
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)