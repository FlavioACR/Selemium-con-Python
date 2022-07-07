# DEMORA IMPLICITA Y EXPLICITA:
# Las pausas ayudan a controlas algunos aspectos de la automatización pero tambíen ayudan con el asincronizmo
# una de las devilidades de selenium.

# IMPLICITA:
# Busca uno o varios elementos en el DOM si no se encuentras disponibles
# por la cantidad del tiempo asignado
# EXPLICITA: Utiliza condiciones de espera determinadas y continúa hasta que se cumplan.

# Librerías:
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# Permite usar las esperas explicitas:
from selenium.webdriver.support.ui import WebDriverWait
# Permite usar las expected condtitios:
from selenium.webdriver.support import expected_conditions as EC


# CLASE DE PRUEBA:
class ExplicitWaitTest(unittest.TestCase):
    '''Caso de prueba de esperas automatizadas'''
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
    
    #  CASOS DE PRUeBA:
    def test_account_link(self):
        ''' Hace referencia al enlace que nos lleva a las cuenta del sitio'''
        # Hacemos referencia al driver y indicamos una espera maxi de 10 sec
        # hasta que se cumpla la condición esperada usando el metodo .until()
        # y apicaremos la condición utilizando un lambda que realiza lo siguiente:
        #       Identifica el elemento por su ID, y obtiene el atributo de length
        #       para saber cuantos elementos hay dentro del elemento buscado y por
        #       ultimo lo igualaremos con 3.
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.ID, 'select-language').get_attribute('length') == '3')

        # Hacemos referencia al enlace de las cuentas con la variable:
        account =  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        # Hacemos click en el enlace de account:
        account.click()

    def test_create_new_customer(self):
        '''Lleva al enlace para la creación de un nuevo usuario'''
        # find_element_by_link_text(acount)click()
        # self.driver.find_element(By.LINK_TEXT, 'ACCOUNT').click()
        self.driver.find_element(By.LINK_TEXT, 'ACCOUNT').click()
    
        my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click()
        
        create_account_bottom = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account_bottom.click()

        WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))
                
    def tearDown(self):
        # Cerrar todo el proceso.
        self.driver.implicitly_wait(8)
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)

