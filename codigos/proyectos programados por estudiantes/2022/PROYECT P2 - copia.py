# print ("Titulares de noticias del 9 de diciembre")
# llamando a la libreria 
from selenium import webdriver 
from selenium.webdriver.common.by import By

# llamando a la variable tiempo para que la pagiana web abra por un lapso de tiempo
# con el fin de que se aprecie de donde viene lo que se va a extraer
import time

# la libreira beautiful soup convierte un archivo html en un lista o matriz
from bs4 import BeautifulSoup
tex = ""

# declaranod el navegador que abrira dicho url
driver = webdriver.Edge()

# escribiendo cual es la pagiana a buscar
url=input('url: ')
# driver.get("https://cnnespanol.cnn.com/2022/12/09/ultimas-noticias-breves-del-mundo-hoy-9-de-diciembre-de-2022/")
driver.get(url)
soup = BeautifulSoup(driver.page_source, "html.parser")
# Mostrando en pantalla lo que realiza la pagina 
# print(soup.text)

# llamando a solamente lo que este en formato \2022\12\09\ultimas-noticias-breves-del-mundo-hoy-9-de-diciembre-de-2022\de titulo y luego imprimiendolo 
# box=soup.find("div", class_="liveblog__title")
print ("\nTitulares de noticias del 9 de diciembre")
tl= soup.find_all("h2")#.get_text()
for a in soup.find_all("h2"):#.get_text():
    print(a)

# time.sleep(5)
# driver.quit()
