# Librerías:

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#chrome = Service(r'C:\Users\Flavio Carrola\Desktop\My learning\chromedriver_win32\chromedriver.exe')
#driver = webdriver.Chrome(service=chrome)


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#driver = webdriver.Chrome(executable_path=r'C:\Users\Flavio Carrola\Desktop\My learning\chromedriver_win32\chromedriver.exe', options=options)