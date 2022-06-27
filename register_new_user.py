# Manejar form, textbox, checkbox y radio button:
from lib2to3.pgen2 import driver
import unittest
from selenium import webdriver
#from pyunitreport import HTMLTestRunner
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class RegisterNewUser(unittest, unittest.TestCase):
    
    def SetUp(self):
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
    

    def teste_new_user(self):
        driver = self.driver
        # Encontrar el elemento y dar un click par adespelgar el menu:
        driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        # Ubicamos el elemento mediante el texto dentro de la variable:
        driver.find_element(By.LINK_TEXT, 'Log In')
        # Ubicamos el crear cuenta y lo asignamos a una variable:
        create_account_button = driver.find_element(By.XPATH, '//*[@id="login-form"]/div/div[1]/div[2]/a')
        # Comprobamos que el boton se encuentr disponible:
        self.assertTrue(create_account_button.is_displayed() and
        create_account_button.is_enabled())
        # Una vez verificado hacermos clic:
        create_account_button.click()



    def tearDown(self):
        # Cerrar todo el proceso.
        self.driver.quit()
    

if __name__ == "__main__":
    unittest.main(verbosity = 2)

    