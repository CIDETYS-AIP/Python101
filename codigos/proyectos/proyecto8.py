#presentar personalidades descritas en 16personalities
import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import re

#proyecto 8
def personalidades():
    '''
    busca personalidades
    '''
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.get('https://www.16personalities.com/personality-types')
    time.sleep(10)
    contenido=bs(driver.page_source,'html.parser')
    a=str(contenido('li',class_='active')[0])
    print(a)
    b=re.findall(r'<div>[A-Za-z \(\)]*</div> ',a)#categorias
    c=re.findall(r'(href="https://www.*")',a)
    print(c)
        
    


if __name__=='__main__':
    personalidades()