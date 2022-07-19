import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



CONSIDERACIONES = '''
* Practica en sitios complejos
* Preguntar acerca acerca de las expectativas
* Define paso a paso el flujo 
* Piensa como usuario final
* Programa como desarrollador
'''
FLUJO_MERCADO_LIBRE = '''
1.Ingresar a mercado libre
2.Selecciona "Colombia"
3.Buscar el Termino "playstation 4"
4.Filtrar por condiciones "Nuevos"
5.Filtrar por ubicación "Bogotá"
6.Ordenar de mayor a menor precio
7.Obtener el nombre y precio de los primeros 5 articulos.
'''
class TestingMercadoLibre(unittest.TestCase):

  def setUp(self):
    # DRIVER

    driver = self.driver
    driver.get('https:www.mercadolibre.com')
    driver.maximize_window()

  def test_search(self):
    driver = self.driver

    # Primer flujo seleccionar País:
    country = driver.find_element(By.ID, 'MX')
    country.click()
    sleep(6)

    # Ubicarse en la Barra
    # e ingresar el texto de busqueda:
    search_field = driver.find_element(By.NAME, 'as_word')
    search_field.click()
    search_field.clear()    
    search_field.send_keys('playstation 4')
    search_field.submit()
    sleep(6)

    # Filtrar por estado:
    # Buscar por le texto parcial del enlace:
    location_filter = driver.find_element(By.LINK_TEXT, 'Distrito Federal')
    location_filter.click()
    sleep(6)

    # Condicion "Nuevos":
    condition_filter = driver.find_element(By.LINK_TEXT, 'Nuevo')
    condition_filter.click()
    sleep(6)

    # Mayor Precio filtro:
    price_major = driver.find_element(By.CLASS_NAME, 'ui-dropdown__link')
    price_major.click()
    # DEPSUES intentarlo con XPATH:
    precio_alto = driver.find_element(By.LINK_TEXT, 'Mayor Precio')
    sleep(6)

    # Información de los primeros 5 articulos:

    articles = []
    prices = []

    for i in range(5):
      tittle = driver.find_element(By.XPATH, f'//*[@id="root-app"]/div/div[2]/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
      articles.append(tittle)

      price = driver.find_element(By.XPATH, f'/*[@id="root-app"]/div/div[2]/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]').text
      price.append()
    print(articles, price)
    
  def tearDown(self):
    self.driver.close()