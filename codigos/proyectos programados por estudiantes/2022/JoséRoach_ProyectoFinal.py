#Enunciado
#Leer todas las carreras que ofrece la UTP en su pagina de oferta academica, y 
# presentar en la terminal de VScode la carrera y el vinculo de la 
#pagina web para dicha carrera.

import os       #Importo esta libreria para el borrado de pantalla
#Creo funciones de acuerdo a la facultad
def civ():
    '''
    presentamos la oferta de carreras de ing. Civil
    '''
    #presentamos la oferta de carreras de ing. Civil
    carr=input('Facultad de Ingenieria Civil\nElija una de las carreras ofertadas:\n1. Lic en Ing en Administracion de Proyectos de Construccion\n2. Lic en Ing Ambiental\n3. Lic en Ing Civil\n4. Lic en Ing Geologica\n5. Lic en Ing Geomatica\n6. Lic en Ing Maritima Portuaria\n7. Lic en Operaciones Maritimas y Portuarias\n8. Lic en Dibujo Automatizado\n9. Lic en Edificaciones\n10. Lic en Saneamiento y Ambiente\n11. Lic en Topografia\n')
    os.system('cls')
    e=0
    match carr:
        case '1':
            print('Lic en Ing en Administracion de Proyectos de Construccion\nLink web: https://fic.utp.ac.pa/licenciatura-en-ingenieria-en-administracion-de-proyectos-de-construccion\n')
        case '2':
            print('Lic en Ing Ambiental\nLink web: https://fic.utp.ac.pa/licenciatura-en-ingenieria-ambiental')
        case '3':
            print('Lic en Ing Civil\nLink web: https://fic.utp.ac.pa/licenciatura-en-ingenieria-civil')
        case '4':
            print('Lic en Ing Geologica\nLink web: https://fic.utp.ac.pa/licenciatura-en-ingenieria-geologica')   
        case '5':
            print('Lic en Ing Geomatica\nLink web: https://fic.utp.ac.pa/licenciatura-en-ingenieria-geomatica')
        case '6':
            print('Lic en Ing Maritima Portuaria\nLink web: https://fic.utp.ac.pa/licenciatura-en-ingenieria-maritima-portuaria')
        case '7':
            print('Lic en Operaciones Maritimas y Portuarias\nLink web: https://fic.utp.ac.pa/licenciatura-en-operaciones-maritimas-y-portuarias')
        case '8':
            print('Lic en Dibujo Automatizado\nLink web: https://fic.utp.ac.pa/licenciatura-en-dibujo-automatizado')
        case '9':
            print('Lic en Edificaciones\nLink web: https://fic.utp.ac.pa/licenciatura-en-edificaciones')    
        case '10':
            print('Lic en Saneamiento y Ambiente\nLink web: https://fic.utp.ac.pa/licenciatura-en-saneamiento-y-ambiente')
        case '11':
            print('Lic en Topografia\nLink web: https://fic.utp.ac.pa/licenciatura-en-topografia')
        case _:
            input('Error, Escriba el numero con la opcion que quisiera elegir')
            os.system('cls')
            e=1
    return e        

def ele():
    carr=input('Facultad de Ingenieria Electrica\nElija una de las carreras ofertadas:\n1. Lic en Ing Electrica y Electronica\n2. Lic en Ing Electrica\n3. Lic en Ing Electronica\n4. Lic en Ing Electromecanica\n5. Lic en Ing en Telecomunicaciones\n6. Lic en Ing Electronica y Telecomunicaciones\n7. Lic en Ing de Control y Automatizacion\n8. Lic en Electronica y Sistemas de Comunicacion\n9. Lic en Sistemas Electricos y Automatizacion\n10. Tec en Ing con especializacion en Autotronica\n11. Tec en Ing con especializacion en Electronica Biomedica\n12. Tec en Ing con especializacion en Sistemas Electricos\n13. Tec en Ing con especializacion en Telecomunicaciones\n')
    os.system('cls')
    e=0
    match carr:
        case '1':
            print('Lic en Ing Electrica y Electronica\nLink web: https://fie.utp.ac.pa/licenciatura-en-ingenieria-electrica-y-electronica\n')
        case '2':
            print('Lic en Ing Electrica\nLink web: https://fie.utp.ac.pa/licenciatura-en-ingenieria-electrica')
        case '3':
            print('Lic en Ing Electronica\nLink web: https://fie.utp.ac.pa/licenciatura-en-ingenieria-electronica')
        case '4':
            print('Lic en Ing Electromecanica\nLink web: https://fie.utp.ac.pa/licenciatura-en-ingenieria-electromecanica')   
        case '5':
            print('Lic en Ing en Telecomunicaciones\nLink web: https://fie.utp.ac.pa/licenciatura-en-ingenieria-en-telecomunicaciones')
        case '6':
            print('Lic en Ing Electronica y Telecomunicaciones\nLink web: https://fie.utp.ac.pa/licenciatura-en-ingenieria-electronica-y-telecomunicaciones')
        case '7':
            print('Lic en Ing de Control y Automatizacion\nLink web: https://fie.utp.ac.pa/licenciatura-en-ingenieria-de-control-y-automatizacion')
        case '8':
            print('Lic en Electronica y Sistemas de Comunicacion\nLink web: https://fie.utp.ac.pa/licenciatura-en-electronica-y-sistemas-de-comunicacion')
        case '9':
            print('Lic en Sistemas Electricos y Automaticacion\nLink web: https://fie.utp.ac.pa/licenciatura-en-sistemas-electricos-y-automatizacion')    
        case '10':
            print('Tec en Ing con especializacion en Autotronica\nLink web: https://fie.utp.ac.pa/tecnico-en-autotronica')
        case '11':
            print('Tec en Ing con especializacion en Electronica Biomedica\nLink web: https://fie.utp.ac.pa/tecnico-en-electronica-biomedica')
        case '12':
            print('Tec en Ing con especializacion en Sistemas Electricos\nLink web: https://fie.utp.ac.pa/tecnico-en-sistemas-electricos')
        case '13':
            print('Tec en Ing con especializacion en Telecomunicaciones\nLink web: https://fie.utp.ac.pa/tecnico-en-telecomunicaciones')        
        case _:
            input('Error, Escriba el numero con la opcion que quisiera elegir')
            os.system('cls')
            e=1
    return e        

def ind():
    carr=input('Facultad de Ingenieria Industrial\nElija una de las carreras ofertadas:\n1. Lic en Ing Industrial\n2. Lic en Ing Logistica y Cadena de Suministro\n3. Lic en Ing Mecanica Industrial\n4. Lic en Ing en Seguridad Industrial e Higiene Ocupacional\n5. Lic en Gestion Administrativa\n6. Lic en Gestion de la Produccion Industrial\n7. Lic en Logistica y Transporte Multimodal\n8. Lic en Mercadeo y Negocios Internacionales\n9. Lic en Recursos Humanos y Gestion de la Productividad\n')
    os.system('cls')
    e=0
    match carr:
        case '1':
            print('Lic en Ing Industrial\nLink web: https://fii.utp.ac.pa/licenciatura-en-ingenieria-industrial\n')
        case '2':
            print('Lic en Ing Logistica y Cadena de Suministro\nLink web: https://fii.utp.ac.pa/licenciatura-en-ingenieria-logistica-y-cadena-de-suministro')
        case '3':
            print('Lic en Ing Mecanica Industrial\nLink web: https://fii.utp.ac.pa/licenciatura-en-ingenieria-mecanica-industrial')
        case '4':
            print('Lic en Ing Seguridad Industrial e Higiene Ocupacional\nLink web: https://fii.utp.ac.pa/licenciatura-en-ingenieria-en-seguridad-industrial-e-higiene-ocupacional')   
        case '5':
            print('Lic en Gestion Administrativa\nLink web: https://fii.utp.ac.pa/licenciatura-en-gestion-administrativa')
        case '6':
            print('Lic en Gestion de la Produccion Industrial\nLink web: https://fii.utp.ac.pa/licenciatura-en-gestion-de-la-produccion-industrial')
        case '7':
            print('Lic en Logistica y Transporte Multimodal\nLink web: https://fii.utp.ac.pa/licenciatura-en-logistica-y-transporte-multimodal')
        case '8':
            print('Lic en Mercadeo y Negocios Internacionales\nLink web: https://fii.utp.ac.pa/licenciatura-en-mercadeo-y-negocios-internacionales')
        case '9':
            print('Lic en Recursos Humanos y Gestion de la Productividad\nLink web: https://fii.utp.ac.pa/licenciatura-en-recursos-humanos-y-gestion-de-la-productividad')    
        case _:
            input('Error, Escriba el numero con la opcion que quisiera elegir')
            os.system('cls')
            e=1
    return e        

def mec():
    carr=input('Facultad de Ingenieria Mecanica\nElija una de las carreras ofertadas:\n1. Lic en Ing Aeronautica\n2. Lic en Ing de Energia y Ambiente\n3. Lic en Ing de Mantenimiento\n4. Lic en Ing Mecanica\n5. Lic en Ing Naval\n6. Lic en Administracion de Aviacion\n7. Lic en Administracion de Aviacion con opcion a vuelo (Piloto)\n8. Lic en Mecanica Automotriz\n9. Lic en Mecanica Industrial\n10. Lic en Refrigeracion y Aire Acondicionado\n11. Lic en Soldadura\n12. Tec en Despacho de Vuelo\n13. Tec en Ing de Mantenimiento de Aeronaves con especializacion en Motores y Fuselajes\n')
    os.system('cls')
    e=0
    match carr:
        case '1':
            print('Lic en Ing Aeronautica\nLink web: https://utp.ac.pa/fim.utp.ac.pa/licenciatura-en-ingenieria-aeronautica\n')
        case '2':
            print('Lic en Ing de Energia y Ambiente\nLink web: https://fim.utp.ac.pa/licenciatura-en-ingenieria-de-energia-y-ambiente')
        case '3':
            print('Lic en Ing de Mantenimiento\nLink web: https://fim.utp.ac.pa/licenciatura-en-ingenieria-de-mantenimiento')
        case '4':
            print('Lic en Ing Mecanica\nLink web: https://fim.utp.ac.pa/licenciatura-en-ingenieria-mecanica')   
        case '5':
            print('Lic en Ing Naval\nLink web: https://fim.utp.ac.pa/licenciatura-en-ingenieria-naval')
        case '6':
            print('Lic en Administracion de Aviacion\nLink web: https://fim.utp.ac.pa/licenciatura-en-administracion-de-aviacion')
        case '7':
            print('Lic en Administracion de Aviacion con opcion a vuelo (Piloto)\nLink web: https://fim.utp.ac.pa/licenciatura-en-administracion-de-aviacion-con-opcion-vuelo')
        case '8':
            print('Lic en Mecanica Automotriz\nLink web: https://fim.utp.ac.pa/licenciatura-en-mecanica-automotriz')
        case '9':
            print('Lic en Mecanica Industrial\nLink web:https://fim.utp.ac.pa/licenciatura-en-mecanica-industrial')    
        case '10':
            print('Lic en Refrigeracion y Aire Acondicionado\nLink web: https://fim.utp.ac.pa/licenciatura-en-refrigeracion-y-aire-acondicionado')
        case '11':
            print('Lic en Soldadura\nLink web: https://fim.utp.ac.pa/licenciatura-en-soldadura')
        case '12':
            print('Tec en Despacho de Vuelo\nLink web: https://fim.utp.ac.pa/tecnico-en-despacho-de-vuelo')
        case '13':
            print('Tec en Ing de Mantenimiento de Aeronaves con especializacion en Motores y Fuselajes\nLink web: https://fim.utp.ac.pa/tecnico-en-ingenieria-de-mantenimiento-de-aeronaves-con-especializacion-en-motores-y-fuselajes')        
        case _:
            input('Error, Escriba el numero con la opcion que quisiera elegir')
            os.system('cls')
            e=1
    return e

def sis():
    carr=input('Facultad de Ingenieria de Sistemas Computacionales\nElija una de las carreras ofertadas:\n1. Lic en Ing de Sistemas de Informacion\n2. Lic en Ing de Sistemas de Informacion Gerencial\n3. Lic en Ing de Sistemas y Computacion\n4. Lic en Ing de Software\n5. Lic en Ciberseguridad\n6. Lic en Ciencias de la Computacion\n7. Lic en Desarrollo de Software\n8. Lic en Informatica Aplicada a la Educacion\n9. Lic en Redes Informaticas\n10. Tecnico en Informatica para la Gestion Empresarial\n')
    os.system('cls')
    e=0
    match carr:
        case '1':
            print('Lic en Ing de Sistemas de Informacion\nLink web: https://fisc.utp.ac.pa/licenciatura-en-ingenieria-de-sistemas-de-informacion\n')
        case '2':
            print('Lic en Ing de Sistemas de Informacion Gerencial\nLink web: https://fisc.utp.ac.pa/licenciatura-en-ingenieria-de-sistemas-de-informacion-gerencial')
        case '3':
            print('Lic en Ing de Sistemas y Computacion\nLink web: https://fisc.utp.ac.pa/licenciatura-en-ingenieria-de-sistemas-y-computacion')
        case '4':
            print('Lic en Ing de Software\nLink web: https://fisc.utp.ac.pa/licenciatura-en-ingenieria-de-software')   
        case '5':
            print('Lic en Ciberseguridad\nLink web: https://fisc.utp.ac.pa/licenciatura-en-ciberseguridad')
        case '6':
            print('Lic en Ciencias de la Computacion\nLink web: https://fisc.utp.ac.pa/licenciatura-en-ciencias-de-la-computacion')
        case '7':
            print('Lic en Desarrollo de Software\nLink web: https://fisc.utp.ac.pa/licenciatura-en-desarrollo-de-software')
        case '8':
            print('Lic en Informatica Aplicada a la Educacion\nLink web: https://fisc.utp.ac.pa/licenciatura-en-informatica-aplicada-la-educacion')
        case '9':
            print('Lic en Redes Informaticas\nLink web: https://fisc.utp.ac.pa/licenciatura-en-redes-informaticas')    
        case '10':
            print('Tec en Informatica para la Gestion Empresarial\nLink web: https://fisc.utp.ac.pa/tecnico-en-informatica-para-la-gestion-empresarial')    
        case _:
            input('Error, Escriba el numero con la opcion que quisiera elegir')
            os.system('cls')
            e=1
    return e

def cie():
    carr=input('Facultad de Ciencias y Tecnologia\nElija una de las carreras ofertadas:\n1. Lic en Ing en Alimentos\n2. Lic en Ing Forestal\n3. Lic en Comunicacion Ejecutica Bilingüe\n')
    os.system('cls')
    e=0
    match carr:
        case '1':
            print('Lic en Ing en Alimentos\nLink web: https://fct.utp.ac.pa/licenciatura-en-ingenieria-en-alimentos\n')
        case '2':
            print('Lic en Ing Forestal\nLink web: https://fct.utp.ac.pa/licenciatura-en-ingenieria-forestal')
        case '3':
            print('Lic en Comunicacion Ejecutiva Bilingüe\nLink web: https://fct.utp.ac.pa/licenciatura-en-comunicacion-ejecutiva-bilingue')   
        case _:
            input('Error, Escriba el numero con la opcion que quisiera elegir')
            os.system('cls')
            e=1
    return e
#Inicio del Programa
f=0
e=1
while f==0:     #El while nos sirve de corrector si en tal caso el usuario escribe un dato no valido 
    fac=input('Elija una facultad:\n1. Ingenieria Civil\n2. Ingenieria Electrica\n3. Ingenieria Industrial\n4. Ingenieria Mecanica\n5. Ingenieria de Sistemas Computacionales\n6. Ciencias y Tecnologia\n')
    os.system('cls')
    f=1
    match fac:
        case '1':
            while e==1:
                e=civ()
        case '2':
            while e==1:
                e=ele()        
        case '3':
            while e==1:
                e=ind()
        case '4':
            while e==1:
                e=mec()
        case '5':
            while e==1:
                e=sis()
        case '6':
            while e==1:
                e=cie()
        case _:
            input('Error, Escriba el numero con la opcion que quisiera elegir')
            os.system('cls')
            f=0    
