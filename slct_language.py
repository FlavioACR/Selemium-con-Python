# MANEJAR DROPDOWNS Y LISTAS:
# Dropdown: Menus despegables, con diferentes opciones.
# Listas: Listas de elementos.

# Librerías:
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# Modulo para manejar dropdown:
from selenium.webdriver.support.ui import Select

# CLASE DE PRUEBA:
class LenguageOptions(unittest.TestCase):
    '''Clase que automatiza la prueba con un menu despegable tipo dropdown, en este caso el dropdown de selección de lenguaje. '''
    
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
    
    def test_select_language(self):
        # Lista de opcione expuestas:
        exp_options = ['English', 'French', 'German']
        # Lista vacia para agregar las opciones "activas" conforme se revises:
        act_options = []

        # Variable para acceder a las opciones del dropdown;
        # Donde llamaremos a la clase "Select" para indicarle donde sencuentra el lenguaje:
        select_language = Select(self.driver.find_element(By.ID, 'select-language'))

        # Validamos que el dropdown, cuente con tres opciones:
        #  El método options permite ingresar directamente a las opciones del dropdown:
        self.assertEqual(3, len(select_language.options))

        # Bucle para iterar cada una de las opciones del dropdown:
        for option in select_language.options:
            # Agregamos a la lista vacia unicamente el teto de la opción:
            act_options.append(option.text)
            # print(act_options)    
        
        # Comprobamos que las listas exp_options & act_options sean iguales:
        self.assertListEqual(exp_options, act_options)

        # Validamos que el Inglés sea el idioma por defecto:
        self.assertEqual('English', select_language.first_selected_option.text)

        # Le decimos al driver que seleccione un idioma del dropdown y para esto utilizaremos 3 opciones;
        # Opción #1; Verificamos que realmente sea el idioma seleccionado usando el texto visible y el URL:
        select_language.select_by_visible_text('German')
        self.assertTrue('store=german' in self.driver.current_url)
        # Opción #2; Atravez del indice;
        # Asignamos a una variable el elemento asigando usando Select y find_by:
        select_language = Select(self.driver.find_element(By.ID, 'select-language'))
        # Le decimos al driver que selccione por el index:
        select_language.select_by_index(0)
        
    def tearDown(self):
        # Cerrar todo el proceso.
        self.driver.implicitly_wait(4)
        self.driver.quit()
    

if __name__ == "__main__":
    unittest.main(verbosity = 2)
