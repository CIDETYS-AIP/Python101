import time
import os
import random
def ELAHORCADO():#Funcion para el juego del Ahoracado
    '''
    documentacion
    '''
    def stickman(fails):#Funcion para imprimir la imagen del ahorcado dependiendo de la cantidad de fallos
        if fails==0:
            print("""
                ---------
                |       |
                |       
                |      
                |       
                |      
                |===============""")
        elif fails == 1:
            print("""
                ---------
                |       |
                |       0
                |    
                |       
                |      
                |      
                |
                |===============""")
        elif fails == 2:
            print("""
                |-------|
                |       |
                |       0
                |    +-◄|
                |       
                |       
                |      
                |
                |===============""")
        elif fails == 3:
            print("""
                |-------|
                |       |
                |       0
                |    +-◄|►-+
                |       
                |       
                |      
                |
                |===============""")
        elif fails == 4:
            print("""
                |-------|
                |       |
                |       0
                |    +-◄|►-+
                |       |
                |       
                |      
                |
                |===============""")
        elif fails == 5:
            print("""
                |-------|
                |       |
                |       0
                |    +-◄|►-+
                |       |
                |       ^
                |      ▬
                |
                |===============""")
        elif fails >= 6:
            print("""
                |-------|
                |       |
                |       0
                |    +-◄|►-+
                |       |
                |       ^
                |      ▬ ▬
                |
                |===============""")
    '''
    documentacion
    '''
    letContador = 0
    palS=0
    juego=0#Se utiliza para finalizar o continuar el juego
    p=0#Funciona como indice de posicion
    a=0#Funciona como indice de posicion
    adivinarPalabra=" "#almacena la palabra que intenta adivinar el jugador
    seleccion=" "#Almacenara la respuesta del jugador para intentar o no adivinar la palabra
    fallos=0#contador de fallos
    continuar=False#Permite que el juego continue siempre que se ingresen datos validos
    ronda=1#lleva la cantidad de rondas
    grupodepalabras=["manzana","luz","programacion","serpiente","azul",
                    "electrocardiograma","esternocleidomastoideo"]#Grupo de palabras posibles para adivinar
    palS=int(input("Ingrese un numero de 1 a "+str(len(grupodepalabras))+": "))#El usuario escoge un numero que corresponde a una palabra de la lista
    while continuar == False:#Se evita que el usuario ingrese un valor fuera de rango
        if palS >= 1 and palS <= 7:
            continuar = True
        else:
            print("Error: número fuera de rango")
            palS=int(input("Ingrese un numero de 1 a "+str(len(grupodepalabras))+": "))
            continuar = False
    palabra=grupodepalabras[palS-1]
    print('*')
    letUsadas=["","","","","","","","","","","","",
    "","","","","","","","","","","","","","",""]#Sirve para evitar que el usuario ingrese la misma letra dos o más veces
    letAdivinadas=["","","","","","","","","","","","","","",
    "","","","","","","","","","","","",""]#va mostrando las letras acertadas de la palabra
    os.system("cls")#limpia la pantalla
    while juego != 1 and p<len(letUsadas):#la condicion para seguir el juego: p se menora a 27 (letras del abecedario) y juego sea diferente de 1
        temp= None 
        if ronda==1:
            stickman(fallos)#Para que se imprima solo la imagen de la horca
        time.sleep(0.5)#Se pausa el programa durante 0.5 segundos
        print("\nLa palabara tiene "+str(len(palabra))+" letras.")#indica cuantas letras tiene la palabra
        print("Ronda #"+str(ronda))#indica el numero de ronda
        letra=input("ingrese una letra: ")#lee la letra ingresada por el usuario
        while (len(letra)!=1 or letra=="1" or letra=="2" or letra=="3" or letra=="4" or
        letra=="5" or letra=="6"or letra=="7" or letra=="8"or letra=="9"):#Evita que se ingrese mas de dos letras o se ingrese numeros
            letra=input("POR FAVOR INGRESE UNA LETRA: ")
        letra=letra.lower()#pone la letra en minúscula
        if ronda == 1:#Cuando se esta en la primera ronda...
            letUsadas[p]= letra#Se almacena la primera letra en la lista de letras usadas
        if ronda > 1:#De la ronda 2 en adelante se ejecuta el siguiente bloque de instrucciones
            for i in range(len(letUsadas)):#Se utiliza un for...
                if letra == letUsadas[i-1]:#para determinar si letra recien ingresada ya se utilizó
                    print("Ya utilizaste la letra "+str(letra))
                    continuar=False
                    break
                else:#de lo contrario "continuar" toma el valor de True para salir de la sentencia repetitiva
                    continuar=True
            if continuar:#Siempre "continuar" tenga el valor de true se almacena la letra ingresada en la lista
                letUsadas[p]=letra
        if continuar:
            a=0#Se reinicia el valor de a en 0
            for d in palabra:#Utilizando un for...
                if d in letra:#Se verifica si la letra ingresada esta en la palabra a adivinar
                    letContador += 1#El contador de letras aumenta por cada letra acertada
                    temp=d#temp toma el valor que posea d
                if d in letUsadas:#Esta funcion se usa para posicionar las letras adivinadas en su lugar
                    letAdivinadas[a]=d
                    a += 1# "a" itera de uno en uno
                else:#Cuando no se adivine una letra se imprime un cuadrado en el espacio de dicha letra
                    letAdivinadas[a]="▇"
                    a += 1# "a" itera de uno en uno
            if letContador < len(palabra):#Siempre que el contador de letras se menor al largo de la palabra...
                print("Letras conseguidas:\n",letAdivinadas,"\n")#Se imprime las letras conseguidas
            if temp is None:#Cuando no se haya encontrado la letra en la palabra...
                fallos += 1#Se incrementa en 1 el contador de fallos
                print("FALLASTE!!")#Y se imprime un mensaje para avisarle al usario que no acerto.
            elif letContador < len(palabra):##Siempre que el contador de letras se menor al largo de la palabra...
                seleccion=input("""Crees saber cuál es la palabra?(S/N)\n
                ADVERTENCIA: Si fallas la palabra contara como 2 fallos: """)#Se da la oportunidad al jugador para adivinar la palabra
                if seleccion=="s" or seleccion == "S":#Si ingresa "S"... 
                    adivinarPalabra=input("Ingresa la palabra: ")#se lee la palabra sugerida del usuario
                    adivinarPalabra=adivinarPalabra.lower()#se pasa toda la palabra a minúscula
                    if adivinarPalabra == palabra:#Si se hace acierta la palabra...
                        print("Adivinaste!!\nLa palabra es: "+str(palabra)+"\nHAS GANADO!!!")
                        juego=1#Se imprime el mensaje de felicitaciones y la palabra, y "juego" tomma el valor de 1 para terminar el juego.
                    else:#Si falla...
                        fallos += 2#El contador de fallos aumenta en 2.
                        print("Que pena, no era esa...\nSigue intentando!!")#Se imprime el respectivo mensaje
            elif letContador == len(palabra):#Cuando el contador de letras acertadas sea igual al largo de la palabra...
                os.system("cls")#Se limpia la pantalla y se imprime el mensaje para decirle al jugador que gano
                print("FELICIDADES HAS GANADO!!!\nPalabra completada:",palabra)
                juego=1
            if fallos>=6:#Si la cantidad de fallos es igual o mayor a 6...
                os.system("cls")#se limpia la pantalla
                print("\nHAS PERDIDO!!")#se le avisa al jugadro que perdió
                print("La palabra era: "+ palabra)#y se muestra cual era la palabra
                juego=1
        p += 1#Se aumenta la variable "p" en 1
        ronda +=1#el contador de rondas aumente
        stickman(fallos)#se llama a la funcion stickman para imprimir la imagen del ahorcado
        os.system("pause")#Se pausa el programa hasta que el usuario presiona cualquier tecla.

def Srcabble():#Funcion para el juego de Srcabble
    puntos=0;puntosBonus=0#puntos normales y puntosBonus
    puntosP1=0;puntosP2=0#puntos del jugador 1 y puntos del jugador 2
    nombreP1=input("Jugador 1 ingrese su nombre: ")#Se ingresa el nombre o alias del jugador 1
    nombreP2=input("Jugador 2 ingrese su nombre: ")#Se ingresa el nombre o alias del jugador 2
    palabrasP1=["","","","",""]#Se almacenan las palabras usadas por el jugador 1
    palabrasP2=["","","","",""]#Se almacenan las palabras usadas por el jugador 2
    def puntaje(pal,bon):#Funcion para determinar el puntaje de cada letra o numero
        diccLetras={"A":1,"B":3,"C":1,"D":2,"E":1,"F":4,"G":2,"H":4,"I":1,"J":8,"K":5,"L":1,"M":3,
                    "N":1,"Ñ":5,"O":1,"P":3,"Q":10,"R":1,"S":1,"T":1,"U":1,"V":4,"W":4,"X":8,"Y":4,
                    "Z":10,"1":7,"2":7,"3":7,"4":7,"5":7,"6":7,"7":7,"8":7,"9":7}
        punt=0;puntB=0#puntos y puntos bonus en la funcion
        for l in pal:#mediante este for...
            punt += diccLetras[l]#Se determina cual es el puntaje de cada letra de la palabra ingresada
        puntB = bon*punt#Los puntos bonus se determina multiplicando el puntaje por el bonus correspondiente
        return punt,puntB#Se retornan puntos y puntos bonus
    for r in range(5):#Se hace un ciclo repetitivo de 5 (5 rondas)
        #Jugador 1
        print("Ronda #",(r+1))#Imprime la ronda actual
        print("Tu turno",nombreP1)
        word1=input("Ingrese la palabra: ")#se lee la palabra ingresada por el usuario
        while len(word1)> 7:#controla que el largo de la palabra no sea mayor a 7
            print("La palabra no puede contener más de 7 letras")
            word1=input("Ingrese la palabra: ")
        word1=word1.upper()#Se convierte toda la palabra en mayúscula
        for repe1 in range(5):#Se verifica que la palabra ingresada no se haya usado previamente
            while word1==palabrasP1[repe1]:
                word1=input("Ya usaste esta palabra, ingresa una diferente: ")
                word1=word1.upper()
        bonusP1= random.randint(1,5)#el bonus se determina aleatoriamente mediante "random.randint"
        puntos,puntosBonus=puntaje(word1,bonusP1)#Se llama a la funcion puntaje y almacenan los valores rentornados en las variables
        print("Puntos de palabra: ",puntos,"\nLa bonificación es de:",bonusP1,"\nTu puntaje total: ",puntosBonus)#se muestra al jugador sus puntos
        puntosP1 += puntosBonus#se va almacenando cada puntaje de palabra en los puntos del jugador 1
        palabrasP1[r]=word1#se almacena la palabra ingresada en la lista
        os.system("pause")#se pausa el programa hasta que el usuario presione cualquier letra.
        os.system("cls")#Se limpia la pantalla para evitar que el jugador 2 vea los datos de jugador 1
                #Jugador 2
        print("Ronda #",(r+1))#Los siguientes bloques son lo mismo que para el jugador 1 pero condicionado al jugador 2
        print("Tu turno",nombreP2)
        word2=input("Ingrese la palabra: ")
        while len(word2)> 7:
            print("La palabra no puede contener más de 7 letras")
            word2=input("Ingrese la palabra: ")
        word2=word2.upper()
        for repe2 in range(5):
            while word2==palabrasP2[repe2]:
                word2=input("Ya usaste esta palabra, ingresa una diferente: ")
                word2=word2.upper()
        bonusP2= random.randint(1,5)
        puntos,puntosBonus=puntaje(word2,bonusP2)
        print("Puntos de palabra: ",puntos,"\nLa bonificación es de:",bonusP2,"\nTu puntaje total: ",puntosBonus)
        puntosP2 += puntosBonus
        palabrasP2[r]=word2
        os.system("pause")
        os.system("cls")
    print("Puntos de",nombreP1,": ",puntosP1,"\nPuntos de",nombreP2,":",puntosP2)
    if puntosP1 > puntosP2:#si el puntaje del jugador 1 es mayor al del jugador 2...
        print(nombreP1,"HA GANADO!!")#el jugador 1 gana
    elif puntosP2 > puntosP1:#si pasa lo contrario...
        print(nombreP2,"HA GANADO!!")#el jugador 2 gana
    else:#En caso de que tenga el mismo puntaje...
        print("ES UN EMPATE!!")#se determina un empate
    if (r+1)==5:#se imprime las palabras usadas por el jugador 1 y jugador 2
        print("Palabras de",nombreP1,":",palabrasP1)
        print("Palabras de",nombreP2,": ",palabrasP2)
    os.system("pause")

#Main
terminar=False#variable para repetir el menu principal
ini=True
while terminar==False:#Se repite siempre que "teminar" tenga el valor de False
    os.system("cls")#Se limpia la pantalla
    if ini:#Solo imprime el mensaje de "bienvenido" cuando se inicie el programa
        print("BIENVENIDO!!")
        ini=False
    opcion=int(input(("Escoge a que deseas jugar:\n1-El ahorcado\n2-Srcabble\n3-Salir\n")))#se lee el numero ingresado por el usuario
    match opcion:#Dependiendo del numero ingresado se ejecuta una instruccion
        case 1:#Se llama a la funcion "ELAHORACADO"
            ELAHORCADO()
        case 2:#Se llama a la función "Srcabble"
            Srcabble()
        case 3:#Se termina la ejecución del programa haciendo que "terminar" tome el valor de True
            print("Hasta la próxima")
            terminar=True
        case _:#Si el numero esta fuera del rango 1-3 se manda un mensaje de error
            print("ERROR: ESTE NUMERO NO ES UNA OPCION")
            os.system("pause")