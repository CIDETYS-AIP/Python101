#buscador de rutas de metrobus
import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import re

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get(r'https://www.mibus.com.pa/red-de-rutas/')
contenido=bs(driver.page_source,'html.parser')

for a in contenido.find_all('tr',class_='route-tr'):
    print(a.text.strip())


time.sleep(10)
driver.quit()

