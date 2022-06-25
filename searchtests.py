# We import the librarys and modules that wee need:
from ast import Pass
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

# Todo se ejecutara en una pestaña diferente:
class searchtst(unittest.TestCase):
    
    def setUp(self):
        # Preparacion del Driver:
        chrome = Service(r"C:\Users\Flavio Carrola\Desktop\My learning\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome(service=chrome)
        driver = self.driver
        # Para ir al sitio:
        driver.get('http://demo-store.seleniumacademy.com/')
        # Maximize la ventana, de acuerdo 
        # a los eleento responsivos que cambian de
        # ubicación u orden dependiendo del tamaño de la vista.
        driver.maximize_window()
        driver.implicitly_wait(14)

    def test_search_texte_field(self):
        # Define como se realizará la busqueda del elemento
        # Se realiza busqueda por el nombre del elemento:
        search_field = self.driver.find_element_by_name("q")    

    def test_search_texte_field_by_class_name(self):
         # Define como se realizará la busqueda del elemento
         # se realiza busqueda por el nombre de la clase:
         search_field = self.driver.find_element_by_class_name("input-text")    

    def test_search_button_enabled(self):
         # Define como se realizará la busqueda del elemento
         # Verificar si un boton se encuentra disponible:
         button = self.driver.find_element_by_class_name("button")    

    def test_count_promo_banner_images(self):
         # Definimos una variable para guardar la lista
         # en este caso una lista distorcionada:
         banner_list = self.driver.find_element_by_class_name("promos")    
         # Definimos una variable en donde se almacenaran
         # los banners, realizando una busqueda dentro de la lista
         # similar a usa expresiones Xpath, mediante el nombre del tag:
         banners = self.driver.find_element_by_tag_name('img')    
         
    def test_vip_promo(self):
        # Identificar con el la ruta Xpath
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div[1]/div[2]/div[2]/div/div/div[2]/ul/li[1]/a/img')

    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_elements_by_css_selector("div.header-minicart span.icon") 


    def tearDown(self):
        # Cerrar todo el proceso.
        self.driver.quit()
    

if __name__ == "__main__":
    unittest.main(verbosity = 2)