from selenium import webdriver
import time 
import re
from bs4 import BeautifulSoup

buscador = webdriver.Chrome()
buscador.get('https://www.mibus.com.pa/red-de-rutas/')

fuente = BeautifulSoup(buscador.page_source, 'html.parser') #Parse interpretador porque esta en html
#**************************
#LISTAR TODAS LAS RUTAS DE METROS BUS EXTRAIDO DESDE EL SITIO WEB MIBUS.COM.PA
#**************************
patron = '[A-Z]\d{3} [(-) Ñ-ñ a-z 0-9 A-Z-]*'

print(buscador.title)

print(re.findall(patron, fuente.text))#extrae todas las ocurrencias que coinciden con el patron

time.sleep(1) #delay para cerrar la pagina
buscador.quit() #cierra la pagina