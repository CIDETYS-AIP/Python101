#Entrar en internet y sacar la informacion 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import re
print("               Estadisticas de instagram")
name = input("Ingrese la cuenta de instagram:\n")

driver = webdriver.Edge()
driver.get("https://www.instagram.com/"+name+"/")
info = BeautifulSoup(driver.page_source, "html.parser")

print(info.text)
#Buscar la informacion requerida de publicaciones, seguidores y seguidos
ldata = []
estadisticas = re.compile(r'(\d{1,3}|\d{1,3},\d{3}|\d{1,3}[KM]|\d{1,3}\.\d{1,3}[KM]|\d{1,3},\d{3}\.\d{1,3}[KM])\s(publicación|publicaciones|seguidor(es)?|seguidos?)')
matches = estadisticas.finditer(info.text)
print(name)
# Quitar las K de mil y las M de millon, y corregir el uso de las , y .
for data in matches:
    print(data.group(0))

    if (data.group(1).endswith("K")==True) or (data.group(1).endswith("K")==True and data.group(1).count(",")==1) or (data.group(1).count(",")==1):
        if data.group(1).count(",")==1 and data.group(1).count(".")==1:
            f1 = data.group(1).replace(",","")
        else:
            f1 = data.group(1)
        f2 = f1.replace("K","")
        # print(f1)
        datacorrection = f2.replace(",",".")
        # print(datacorrection)
        list = [data.group(2),float(datacorrection)*1000]
        ldata.append(list)

    elif (data.group(1).endswith("M")==True) or (data.group(1).endswith("M")==True and data.group(1).count(",")==1):
        if data.group(1).count(",")==1 and data.group(1).count(".")==1:
            f1 = data.group(1).replace(",","")
        else:
            f1 = data.group(1)
        f2 = f1.replace("M","")
        # print(f1)
        datacorrection = f2.replace(",",".")
        # print(datacorrection)
        list = [data.group(2),float(datacorrection)*1000000]
        ldata.append(list)
    else:
        list = [data.group(2),float(data.group(1))]
        ldata.append(list)

# print(ldata)

time.sleep(5)
driver.quit()




# Crear gráfica en excel
from openpyxl import Workbook

from openpyxl.chart import (PieChart, Reference)

file = open("Estadisticas de "+name+".xlsx", "w")
file.close()

libro = Workbook()
excel = libro.active
# Escrbir la información
for row in ldata:
    excel.append(row)
# indicar uso de gráfica de pie
pieinsta = PieChart()
# selecionar las celdas para hacer la gráfica
labels = Reference(excel, min_col=1, min_row=2, max_row=3)
ldata = Reference(excel, min_col=2, min_row=1, max_row=3)
# definir que es la linea de valores y la de categorias
pieinsta.add_data(ldata, titles_from_data=True)
pieinsta.set_categories(labels)
# titulo de la gráfica
pieinsta.title = "seguidores Vs seguidos"
# Celda donde poner la gráfica
excel.add_chart(pieinsta,"D2")
libro.save("Estadisticas de "+name+".xlsx")
