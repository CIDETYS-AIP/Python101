#buscador de amazon 
#presentar precio, rating, nombre del articulo y vinculo del articulo
import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import re

cuenta=input('Introduzca cuenta de instagram: ')
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get('https://www.instagram.com/'+cuenta)

time.sleep(15)

#read following, followers and posts
contenido=bs(driver.page_source,'html.parser')
datos=str(contenido)
res=re.search(r'(\d* Followers), (\d* Following), (\d* Posts)',datos)

if res!=None:
    print(res[1])
    print(res[2])
    print(res[3])

#log out
time.sleep(10)

driver.quit()