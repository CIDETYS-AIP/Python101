#transformacion de 5 monedas a USD y viceverrsa
import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import re

print('Cambio de moneda entre USD y cualquier moneda de su eleccion')
a=''
c=''
while c=='':
    moneda2=input('1. Euro (EUR)\n2. Yen Japones (JPY)\n3. Renminbi (CNY)\n4. Libra Esterlina (GBP)\n5. Peso Mexicano (MXN)\nEscoga el numero de su eleccion: ')
    match moneda2:
        case '1':
            c='EUR'
        case '2':
            c='JPY'
        case '3':
            c='CNY'
        case '4':
            c='GBP'
        case '5':
            c='MXN'
        case _:
            print('Escoga nuevamente')
b='USD to '+c

#extrae la informacion de cambio de internet
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get('https://www.google.com')
busqueda=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
busqueda.send_keys(b)
busqueda.send_keys(Keys.ENTER)

cambio=bs(driver.page_source,'html.parser')
time.sleep(10)
driver.quit()

#realiza la operacion numerica de cambio entre monedas
a=re.search(r'data-value="([\d.]+)"',str(cambio))
print('1 dolar americano (USD) equivale a: ',a[1],' ',c)

moneda1=input('1. USD\n2. '+c+'\nMoneda de origen: ')
conversion=float(input('Ingrese el monto: '))
if moneda1=='1':
    print('Dolares: ',conversion,c,': ',conversion*float(a[1]))
else:
    print(c,': ',conversion,' Dolares: ',conversion/float(a[1]))




