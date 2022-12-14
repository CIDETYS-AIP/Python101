# #convertidor de moneda USD a EUR (1USD=0.96EUR)
# var=0.0 #define variable como flotante
# total=0.0
# var=20.0
# total=var*(0.96/1)
# print('{:.5f}'.format(total))

#bienvenida personalizada
# nombre=input('Como te llamas: ')
# print('Buen dia',nombre)

#creacion de un archivo de texto por su nombre
# nombre=input('nombre: ')
# open(nombre+'.txt','w')

#extraccion de 2 primeras y 2 ultimas letras de cualquier palabra
#palabra=input('ingrese palabra: ')
#print("las primeras 2 letras: ",palabra[0:2],'\nlas ultimas 2 letras: ', palabra[-2:])

# actividad lista
# x = 5
# lista = [1,'hola',True,x,[1,2,'2',False]]
# print(lista)
# lista[0] = 'HOLA'
# lista[4][2] = 'como estas'
# lista[5] = 'nuevo'
# print(lista)
# lista + 'nuevo'
# print(lista)

#actividad tupla
# tupla = (1,'2',True)
# print(tupla[:2])

#actividad diccionario
# dicc = {'numero' : 1,
#     'alfanumerico' : 'hola',
#     'bolean' : True,
#     'lista' : [1,2,3,'hola como tas'],
#     'tupla' : (8,7,6,"al reves"),
#     'diccionario' : {'saludar':'hola',2:'soy 2'},
#     1 : 'pro'
# }
# print(dicc)

# #print('\n',dicc['lista'][2])
# #print('\n',dicc['tupla'])
# #print('\n',dicc['diccionario'][saludar])
# dicc['lista'] = 'bienvenidos a la clase de python'
# print('\n',dicc)

# metodos de alfanumericos
# alfa = input('ingrese la oracion: ')
# # alfa = alfa.capitalize()
# # print(alfa)
# # print(alfa.lower())
# # print(alfa.upper())
# # print(alfa.count('a'))
# # print(len(alfa))
# print(alfa.isalnum(),alfa.isalpha())

#metodos de lista
# lista = ['hola','manue','celular','pantalla','carro','reloj']
# print(lista)
# # lista.append(input('agrege el elemento: '))
# #lista.insert(0, input('inicio: '))
# #lista.remove('adios')
# #lista.sort()
# lista.clear()
# print('\n',lista)

#metodos de diccionarios
# dicc = {'numero' : 1,
#     'alfanumerico' : 'hola',
#     'bolean' : True,
#     'lista' : [1,2,3,'hola como tas'],
#     'tupla' : (8,7,6,"al reves"),
#     'diccionario' : {'saludar':'hola',2:'soy 2'},
#     1 : 'pro'
# } 
# print(dicc.clear())
# print('\n',dicc)

#metodos de archivos
f = open('archivo.txt', 'a')
f.write(" se you soon")
f.close()

f = open('archivo.txt', 'r')
print('\n',f.read())