# Librerías:
from cgitb import text
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# CLASE DE PRUEBA:
class DynamicControls(unittest.TestCase):
    '''Manejo de controles Dinamicos con esperas'''
    def setUp(self):
        # Preparacion del Driver:
        chrome = Service(r'C:\Users\Flavio Carrola\Desktop\My learning\chromedriver_win32\chromedriver.exe')
        self.driver = webdriver.Chrome(service=chrome)
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Dynamic Controls').click()
            
    #  CASOS DE PRUeBA:
    def test_dynamic_control(self):
        driver = self.driver

        # Identificar y hacer cliek en el checkbox:
        checkbox = driver.find_element(By.CSS_SELECTOR, 'checkbox > input[type=checkbox]')
        checkbox.click()
        
        # Identificar el elemento para remover y hacer click:
        remove_add = driver.find_element(By.CSS_SELECTOR,'checkbox > input[type=checkbox]')
        remove_add.click()

        # Esperar Hasta que se pueda hacer click en el elemento:
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'checkbox > input[type=checkbox]')))
        remove_add.click()

        #SEGUNDOS CONTROLES:   
        enabledisable_button = driver.find_element(By.CSS_SELECTOR,'#input-example > button')  
        enabledisable_button.click()
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > button')))

        # Identificamos el area de Texto:
        text_area = driver.find_element(By.CSS_SELECTOR, '#input-example > input[type=text]')
        text_area.click()
        # Ingresamos texto:
        text_area.send_keys('Python con Selenium :D')
        text_area.submit()

    def tearDown(self):
        # Cerrar todo el proceso.
        self.driver.implicitly_wait(8)
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)