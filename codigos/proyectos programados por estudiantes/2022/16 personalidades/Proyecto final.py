# Librerias importadas para el programa. 
# BeautifulSoup para extraer el codigo fuente de la pagina a buscar
# Request para obtener el url de la página a la cual haremos la extracción
# Textblob para traducir la informacion extraida al español

from bs4 import BeautifulSoup as c
import requests
from textblob import TextBlob

#Esta sería la funcion para traducir la informacion extraida del idioma ingles al español

def traducir(n):
   eb=TextBlob(n)
   return print(eb.translate(from_lang='en',to='es'))

#Esta funcion retorna el texto limpio de la informacion que se encuentra dentro del div con 
# class definition que contiene la definicion de la personalidad

url='valor'
def imprimir(url):
 html= requests.get(url)
 content= html.content
 soup=c(content,'html.parser')
 Descripcion=soup.find('div',{'class':'definition'})
 return Descripcion.text

# El programa define la personalidad que quiera saber el usuario extrayendo la
# informacion de una pagina del sitio 16personalities 
# dependiendo de cual es la personalidad que quiere saber el usuario.
# Use if-else para que el usuario seleccione la pagina con los numeros del 1 al 4. 
# Cualquier otro valor hace que la programa diga que el valor es incorrecto
# y pare sin imprimir ningun resultado

a='valor'
b='valor'
d='valor'
while True:
 print('\t\t\t\tDescubridor de personalidades\n')
 a=input('Diga el tipo de personalidad de la que quiere saber(1=Analista, 2=Diplomatico, 3=Centinelas, 4=Explorador): ')
 if a=='1':
    b=input('Diga el tipo de personalidad analista que quiere saber(1=Arquitecto,2=Logico,3=Comandante,4=Debate): ')
    if b=='1':
       d=(imprimir('https://www.16personalities.com/intj-personality'))
       traducir(d)
       break
    if b=='2':
       d=imprimir('https://www.16personalities.com/intp-personality')
       traducir(d)
       break
    if b=='3':
       d=imprimir('https://www.16personalities.com/entj-personality')
       traducir(d)
       break
    if b=='4':
       d=imprimir('https://www.16personalities.com/entp-personality')
       traducir(d)
       break
    else:
        print('Opcion incorrecta corra el programa de nuevo')
        break
 if a=='2':
    b=input('Diga el tipo de personalidad diplomata que quiere saber(1=Defensor,2=Mediador,3=Protagonista,4=Activista): ')
    if b=='1':
       d=imprimir('https://www.16personalities.com/infj-personality')
       traducir(d)
       break
    if b=='2':
       d=imprimir('https://www.16personalities.com/infp-personality')
       traducir(d)
       break
    if b=='3':
       d=imprimir('https://www.16personalities.com/enfj-personality')
       traducir(d)
       break
    if b=='4':
       d=imprimir('https://www.16personalities.com/enfp-personality')
       traducir(d)
       break
    else:
        print('Opcion incorrecta corra el programa de nuevo')
        break
 if a=='3':
    b=input('Diga el tipo de personalidad Centinela que quiere saber(1=Logistico,2=Defensor,3=Ejecutivo,4=Consul): ')
    if b=='1':
       d=imprimir('https://www.16personalities.com/istj-personality')
       traducir(d)
       break
    if b=='2':
       d=imprimir('https://www.16personalities.com/isfj-personality')
       traducir(d)
       break
    if b=='3':
       d=imprimir('https://www.16personalities.com/estj-personality')
       traducir(d)
       break
    if b=='4':
       d=imprimir('https://www.16personalities.com/esfj-personality')
       traducir(d)
       break
    else:
        print('Opcion incorrecta corra el programa de nuevo')
        break
 if a=='4':
    b=input('Diga el tipo de personalidad Polemista que quiere saber(1=Virtuoso,2=Aventurero,3=Emprendedor,4=Artista): ')
    if b=='1':
       d=imprimir('https://www.16personalities.com/istp-personality')
       traducir(d)
       break
    if b=='2':
       d=imprimir('https://www.16personalities.com/isfp-personality')
       traducir(d)
       break
    if b=='3':
       d=imprimir('https://www.16personalities.com/estp-personality')
       traducir(d)
       break
    if b=='4':
       d=imprimir('https://www.16personalities.com/esfp-personality')
       traducir(d)
       break
    else:
        print('Opcion incorrecta corra el programa de nuevo')
        break
 else:
    print('Opcion incorrecta corra el programa de nuevo')
    break
