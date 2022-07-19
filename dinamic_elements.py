# Librerías:
import unittest
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
        driver.find_element(By.LINK_TEXT, 'Disappearing Elements').click()
            
    #  CASOS DE PRUeBA:
    def test_name_elements(self):
        driver = self.driver

        # Acceder a cada uno de los elementos:
        # Lista de opciones vacia:
        options = []
        # Opciones del menu
        menu = 5
        # Intentos:
        tries = 1

        # Explica el codigo:
        # Mientras que la longitud de options sea menor a 5 
        while len(options) < 5:
            # limpiar el contenido de la lista options:
            options.clear()

        # Iteraremos en cada una de las opciones del menu:
            for i in range(menu):
                try:
                    # BUSQUEDA DEL ELEMENTO
                    # Tomamos el xpath del primer elemento y agregamo un formato para modificar el numero de la lista
                    # y asi solamente  usar un xpath:
                    options_name = driver.find_element(By.XPATH, f'//*[@id="content"]/div/ul/li[{i + 1}]/a')
                    # Agregamos el elemento a la lista options:
                    options.append(options_name)
                    # bUSCAR un pRint para impRimir el nombre DEL BOtON.
                    # print(options)
                except:
                    # En caso de no encontrar el elementos:
                    # Imprimir este mensaje:
                    print(f'Options number {i + 1} is NOT FOUND')
                    # Sumamos uno al numero de intentos:
                    tries += 1
                    # Y refrescamos el sitio:
                    driver.refresh()

        print(f'Finished in {tries} tries')            
    
    def tearDown(self):
        # Cerrar todo el proceso.
        self.driver.implicitly_wait(8)
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)