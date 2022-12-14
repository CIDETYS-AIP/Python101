##amazon
# selenium 4
# from selenium import webdriver
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from bs4 import BeautifulSoup as bs

# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# driver.get(r'https://www.amazon.com')

# a=driver.page_source

# soup=bs(a,'html.parser')
# print(soup.text)
# driver.close()

##juegos
import os
import re

def scrabble():
    print('juego')
    return

def ahorcado(palabra=''):
    #transforma palabra en *
    if palabra=='':
        palabra=input('ingrese palabra: ').lower()
    os.system('cls')
    z='*'*len(palabra) 
    print(z)

    #juego 
    #3 intentos
    intentos=3
    historial=[]
    while intentos>0:
        letra=input('ingrese letra: ').lower()
        if letra.lower() in historial:
            print('Ya introdujo la letra anteriormente')
        else:
            #nueva letra
            historial.append(letra)
            if letra not in palabra:
                intentos-=1
            else:#letra presente en la palabra original
                print('pendiente')
            print(z)
            if z==palabra:
                print('palabra finalizada')
                break
    return

while True:
    print('elija juego')
    a=input('scrabble(1), ahorcado(2) o salir(3): ')
    match a:
        case '1':
            scrabble()
        case '2':
            ahorcado()
        case '3':
            break
        case other:
            print('error de seleccion')

#buscador de paradas de metrobus

#extraccion de texto de un pdf/image

#extraccion de data de una red social

#data de covid

#transformacion de 5 monedas a USD 
# from selenium import webdriver
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from bs4 import BeautifulSoup as bs

# monedas=['eur']

# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# driver.get(r'https://www.google.com')

# a=driver.page_source

# soup=bs(a,'html.parser')
# print(soup.text)
# driver.close()

# #extraccion de data de 16personalities.com
# from selenium import webdriver
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from bs4 import BeautifulSoup as bs

# monedas=['eur']

# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# driver.get(r'https://www.16personalities.com/personality-types')

# a=driver.page_source
# soup=bs(a,'html.parser')
# print(soup.text)
# driver.close()

#calculadora de 9 tipos de factorizacion

#data del mundial por pais solicitado

#automatizacion de tareas