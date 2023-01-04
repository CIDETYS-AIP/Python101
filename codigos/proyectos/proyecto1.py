#buscador de amazon 
#presentar precio, rating, nombre del articulo y vinculo del articulo
import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#proyecto 1
def amazon(item=''):
    '''
    buscador de productos en amazon
    '''
    if item=='':
        item=input('introduzca elemento que desea buscar')
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.get('https://www.amazon.com')

    barra=driver.find_element(By.ID,"twotabsearchtextbox")

    barra.send_keys(item)
    barra.send_keys(Keys.ENTER)

    contenido=bs(driver.page_source,'html.parser')

    for a in contenido.find_all('div',class_='s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border'):
        #articulo
        for b in a.findAll(class_=['a-price','a-size-medium a-color-base a-text-normal','a-row a-size-small']):
            if 'out of 5 stars' in b.text:
                print('rating: ',end='')
            elif "$" in b.text:
                print('precio: ',end='')
            else:
                print('articulo: ',end='')
            print(b.text)
            print('\n\n\n')


    time.sleep(10)
    driver.quit()

if __name__=='__main__':
    amazon()