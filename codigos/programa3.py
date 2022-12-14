# #datos solicitados: nombre, apellido, edad, carrera, correo
# #utilizando variables (no recomendado)
# nombre=input('Ingrese su nombre: ')
# apellido=input('Ingrese su apellido: ')
# edad=input('Ingrese su edad: ')
# carrera=input('Ingrese su carrera: ')
# correo=input('Ingrese su correo: ')

# nombre=nombre.capitalize()
# apellido=apellido.capitalize()
# carrera=carrera.capitalize()
# correo=correo.capitalize()
# #la edad es un numero por ende no se capitaliza
# with open(nombre+'.txt','w') as file:
#     file.write(nombre+'\n')
#     file.write(apellido+'\n')
#     file.write(edad+'\n')
#     file.write(carrera+'\n')
#     file.write(correo+'\n')
# file.close()

# # #utilizando listas
# # datos=[]
# # datos.append(input('ingrese su nombre: '))
# # datos.append(input('ingrese su apellido: '))
# # datos.append(input('ingrese su edad: '))
# # datos.append(input('ingrese su carrera: '))
# # datos.append(input('ingrese su correo: '))

# # datos[0]=datos[0].capitalize()
# # datos[1]=datos[1].capitalize()
# # datos[3]=datos[3].capitalize()
# # datos[4]=datos[4].capitalize()

# # #opcion1 
# # with open('lista'+datos[0]+'.txt','w') as file:
# #     file.write(datos[0]+'\n')
# #     file.write(datos[1]+'\n')
# #     file.write(datos[2]+'\n')
# #     file.write(datos[3]+'\n')
# #     file.write(datos[4]+'\n')
# # file.close()

# # #opcion2
# # f=open('lista2'+datos[0]+'.txt')
# # f.writelines(datos)
# # f.close()
    
# # #utiliando diccionarios
# # datos2={}
# # datos2['nombre']=input('ingrese su nombre: ')
# # datos2['apellido']=input('ingrese su apellido: ')
# # datos2['edad']=input('ingrese su edad: ')
# # datos2['carrera']=input('ingrese su carrera: ')
# # datos2['correo']=input('ingrese su correo: ')

# # datos2['nombre']=datos2['nombre'].capitalize()
# # datos2['apellido']=datos2['apellido'].capitalize()
# # datos2['carrera']=datos2['carrera'].capitalize()
# # datos2['correo']=datos2['correo'].capitalize()

# # #opcion1
# # with open('diccionario'+datos2['nombre']+'.txt','w') as file:
# #     file.write(datos2['nombre']+'\n')
# #     file.write(datos2['apellido']+'\n')
# #     file.write(datos2['edad']+'\n')
# #     file.write(datos2['carrera']+'\n')
# #     file.write(datos2['correo']+'\n')
# # file.close()

# # #opcion2
# # f=open('diccionario2'+datos2['nombre']+'.txt','w')
# # f.write(str(datos2))
# # f.close()

# # #aplica para todos los tipos de archivo
# # #opcion1
# # with open(nombre+'.txt','r') as file:
# #     print(file.readlines())
# # file.close()

# # #opcion2
# f=open(nombre+'.txt')
# print(f.read())
# f.close()

#-------------------------
#debug actividad
# div = input('ingrese divisor: ')
# div1 =input('ingrese el dividendo:')
# try:
#     tol = div/div1
# except:
#     tol = int(div)/int(div1)
# print(tol)
# bucle for actividad
# suma = 0
# for i in range(101):
#     suma += i
# print(suma)

# palabra = input('ingrese palabra a deletrear: ')
# for i in palabra:
#     print(i)

# lista = ['hola','como','estan','que tal']
# for i in lista:
#     print(i)
#     for y in i:
#         print(y)

# num = int(input('numero: '))
# for i in range(0, num, 2):
#     print( i )

# dic = {
#     'primer' : 'hola',
#     'segundo' : 2,
#     'tercero' : 'lis',
#     'cuarto' : 3
# }
# for i, j in dic.items():
#     print(j)

# Bucles While Actividad
# suma = 0
# x = 0
# while x <= 100:
#     suma += x
#     x += 1
# print(suma)

# palabra = input('a deletrear')
# x = 0
# print(len(palabra))
# while x < len(palabra):
#     print(palabra[x])
#     x += 1

# lista = [1,"hola",3,4]
# x = 0
# while x < len(lista):
#     print(lista[x])
#     x += 1 

# num = int(input('numero: '))
# x = 0
# while x <= num:
#     print(x)
#     x += 2

# Decision if and mactch actividad
# i = 'valor'
# suma = 0
# impu = 'hola'
# t = 'x'
# while i != '0':
#     i = input('inserte valor del articulo o 0 para temrinar: ')
#     t = input('paga impuesto si o no: ')
#     if t == 'si':
#         suma += float(i)*(1+0.7)
#     else:
#         suma += float(i)
# print(suma)

# def suma(a,b):
#     res = float(a)+float(b)
#     return res

# def divi(a,b):
#     res = float(a)/float(b)
#     return res

# def mult(a,b):
#     res = float(a)*float(b)
#     return res

# print((suma(5,6)))
# print(int(divi(5,6)))
# print(int(mult(5,6)))

# def che(a):
#     print(type(a))
#     return

# che('manuel')