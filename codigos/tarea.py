#maquina registradora usando if (con o sin impuesto de 1.07)
# art=''
# total=0
# while art!='f':
#     art=input('ingrese precio de articulo. Si el articulo lleva impuesto coloque una "i" al final del precio. "f" para salir del programa: ')
#     if art[-1].isdigit():
#         total+=float(art)
#     else:
#         if art.lower()=='f':
#             break
#         else:
#             total+=float(art[:-1])*1.07
# print(total) 
    
#maquina registradora utilizando match (0%, 7% y 10%)
# art=''
# total=0
# while art!='f':
#     art=input('ingrese precio de articulo. \nSi el articulo lleva 7%, coloque una "i" al final; \nsi lleva 10%, coloque un "d" al final del producto; \ndel precio. "f" para salir del programa: ')
#     match art[-1].lower():
#         case 'i':
#             total+=float(art[:-1])*1.07
#         case 'd':
#             total+=float(art[:-1])*1.1
#         case 'f':
#             break
#         case _:
#             total+=float(art)
# print(total)

# #calculadora de areas y perimetros
# while True:
    # forma=input('1. Cuadrado\n2. Circulo\n3. Triangulo\n4. Salir\nEscoga figura: ')
    # match forma:
    #     case '1':
    #         l=float(input('lados: '))
    #         print('area: ',l**2)
    #         print('perimetro: ',l*4)
    #     case '2':
    #         l=float(input('radio: '))
    #         print('area: ',l**2*3.14)
    #         print('circunferencia: ',l*2*3.14)
    #     case '3':
    #         l=float(input('base: '))
    #         m=float(input('altura: '))
    #         print('area: ',l*m/2)
    #         print('perimetro: ',3*l)
    #     case '4':
    #         break
    #     case _:
    #         print('opcion/ incorrecta')

#convertidos de monedas
# print('Se hara la transformacion de cualquier moneda a USD')
# while True:
#     moneda=input('1.Euro (EUR)\n2.Yen (Y)\n3.Libra (L)\nEscoja la moneda: ')
#     if moneda.isdigit():
#         dinero=input('introduzca la cantidad: ')
#         match moneda:
#             case '1':
#                 print('tranformacion euro')
#                 cambio=0.96
#             case '2':
#                 print('tranformacion yen')
#                 cambio=1.1
#             case '3':
#                 print('transformando libra')
#                 cambio=0.1
#             case _:
#                 print('opcion no valida')
#                 print('se saldra del programa')
#                 break
#         print(float(dinero)*cambio)
#     else:
#         print('la opcion seleccionada no es numerica')

#convertidor de temperaturas
# while True:
#     eleccion=input('1. Centigrado a farenheit\n2. Farenheit a Centigrados\nEscoga 1 opcion: ')
#     if eleccion.isdigit():
#         grados=input('Ingrese los grados: ')
#         if eleccion=='1':
#             print('Centigrado a farenheit')
#             print(float(grados)*9/5+32)
#         else:
#             print('Farenheit a Centigrado')
#             print((float(grados)-32)*5/9)
#     else:
#         print('opcion no numerica\n se saldra del programa')
#         break

def fib(n):
    #metodo 1
    # if n<=1:
    #     return 1
    # else:
    #     return fib(n-1)+fib(n-2)
    
    #metodo 2
    a,b,c=0,1,0
    while c<n:
        yield b
        a,b=b,a+b
        c+=1
    
# for a in range(10):
#     b=fib(a)
#     print(a,'.',b)
fibo=[a for a in fib(100)]
print(fibo)
# print(fib(12))