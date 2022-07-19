# Librerías:
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


# CLASE DE PRUEBA:
class Tables(unittest.TestCase):
    '''Automatización de la examinación del texto de un sitio web'''
    def setUp(self):
        # Preparacion del Driver:
        chrome = Service(r'C:\Users\Flavio Carrola\Desktop\My learning\chromedriver_win32\chromedriver.exe')
        self.driver = webdriver.Chrome(service=chrome)
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Sortable Data Tables').click()
            
    #  CASOS DE PRUEBA:
    def test_sort_table(self):
        driver = self.driver

        # Creamos una lista 'vacia' donde se guardaran sublistas,
        # que contiene un list comperhersion enfocado al numero de columnas:
        table_data = [[]for i in range(5)]
        print(table_data)

        # Iteraremos por cada una de las series de datos:
        for i in range(5):
            # Variable que identifica el header de la tabla:
            # Esta variable contiene el xpath de la primer columna pero la expresión contiene un elemento
            # importante que es el ultimo tn[1], agregaremos el 'f' string, antes de la expresión del xpath y 
            # el tn[i], será sustituido por el iterador 'i', de este modo th[{i + 1}, para poder iterar todos los header de la columnas:
            header = driver.find_element(By.XPATH, f'//*[@id="table1"]/thead/tr/th[{i + 1}]/span')
            # Agregamos el header a la lista table_data:
            table_data[i].append(header.text)

            # Creamos un ciclo anidado para iterar en los datos:
            for j in range(4):
                 row_data = driver.find_element(By.XPATH, f'//*[@id="table1"]/tbody/tr[{j + 1}]/td[{j + 1}]')
                 table_data[i].append(row_data.text)

            # RETO AGREGAR El WEBSITE;

        print(table_data)

    def tearDown(self):
        # Cerrar todo el proceso.
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)