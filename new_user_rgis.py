# Manejar form, textbox, checkbox y radio button:

# Librerías:
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class SearchTests(unittest.TestCase):
    
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
    
    def teste_new_user(self):
        driver = self.driver

        # Encontrar el elemento y dar un click para desplegar el menu de ACCOUNT:
        driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/a/span[2]').click()

        # Ubicamos el elemento mediante el texto dentro de la variable:
        driver.find_element(By.LINK_TEXT, 'Log In').click()
        
        # Ubicamos el crear cuenta y lo asignamos a una variable:
        create_account_button = driver.find_element(By.XPATH, '//*[@id="login-form"]/div/div[1]/div[2]/a')

        # Comprobamos que el boton se encuentr disponible:
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        # Una vez verificado hacermos clic:
        create_account_button.click()
        
        # Verificamos que realemente estemos dentro del sitio de registro de cuenta,
        # utilizando el titulo como medio de verificación:
        self.assertEqual('Create New Customer Account', driver.title)

        # Creamos una serie de variables que nos permitirán identificar los campos
        # de registro del nuevo usuario:
        first_name = driver.find_element(By.ID, 'firstname')
        middle_name = driver.find_element(By.ID, 'middlename')
        last_name = driver.find_element(By.ID, 'lastname')
        email_address = driver.find_element(By.ID, 'email_address')
        password = driver.find_element(By.ID, 'password')
        confirm_password = driver.find_element(By.ID, 'confirmation')
        register_news = driver.find_element(By.ID, 'is_subscribed')
        sign_up_button = driver.find_element(By.XPATH, '//*[@id="form-validate"]/div[2]/button')

        # Verificamos la disponibilidad de cada una de las variables:
        self.assertTrue(first_name.is_enabled()
        and middle_name.is_enabled()
        and last_name.is_enabled()
        and email_address.is_enabled()
        and register_news.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and sign_up_button.is_enabled())

        # Validación mandando datos a cada uno de los campos:
        first_name.send_keys('Test')
        middle_name.send_keys('Test')
        last_name.send_keys('Test')
        email_address.send_keys('Test@gmail.com')
        register_news.send_keys('Test')
        password.send_keys('Test')
        confirm_password.send_keys('Test')
        sign_up_button.send_keys('Test')
        sign_up_button.click()

        
    def tearDown(self):
        # Cerrar todo el proceso.
        self.driver.quit()
    

if __name__ == "__main__":
    unittest.main(verbosity = 2)
