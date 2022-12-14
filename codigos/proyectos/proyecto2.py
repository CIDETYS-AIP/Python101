#juegos de scrabble y el ahorcado

def ahorcado(palabra=''):
    if palabra=='':
        palabra=input('ingrese la palabra para jugar: ')
    print('*'*len(palabra))
    z='*'*len(palabra)
    intentos=3
    letras=[]
    while z!=palabra and intentos>0:
        letra=input('ingrese letra: ')
        if letra in letras:
            print('letra ya jugada')
        elif letra in palabra:
            letras.append(letra.lower())
            for a,b in enumerate(palabra):
                if b==letra.lower():
                    z=z[:a]+letra.lower()+z[a+1:]
        else:
            intentos-=1
        print(z)
    if intentos==0:
        print('perdiste')
    else:
        print('ganastes')
if __name__=='__main__':
    print('juguemos')
    ahorcado()
