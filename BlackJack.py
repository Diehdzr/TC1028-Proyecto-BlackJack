'''
Estaba pensando en mejor hacer un sistema de apuestas donde se inicia con 100 fichas 
y el usuario escoja que apuesta hacer

Pensaba también hacer una funcion que permita doblar la mano como en blackjack
'''

'''Posiblemente me este adelantando, pero ya conocia que existia
esta biblioteca, entonces la investigue
un poco para añadirla a una pequeña función
'''

import random

#FUNCIONES BÁSICAS

def poner_apuesta(fichas, apuesta):
    if apuesta <= 0:
        return "Apuesta invalida"
    elif apuesta > fichas:
        return "Apuesta excede fichas"
    return apuesta

def doblar_apuesta(apuesta, fichas):
    if apuesta * 2 > fichas:
        return apuesta
    return apuesta * 2
    
#como mencione, use la biblioteca de random para hacer esta función
#docs.python.org/es/3.10/library/random.html

def repartir_carta():
    return random.randint(1,11)

#Funcion para contar las cartas
def sumar_cartas(cartas):
    sum = 0
    for n in cartas:
        sum = sum + n
    return sum

# Operadores de comparación para definir resultado

def determinar_fichas(usuario, compu, apuesta, fichas):
    if usuario > 21:
        fichas = fichas - apuesta
    elif compu > 21:
        fichas = fichas + apuesta
    elif usuario > compu:
        fichas = fichas + apuesta
    elif compu > usuario:
        fichas = fichas - apuesta
    elif usuario == compu:
        fichas = fichas

    return fichas
    

#----------Programa principal -------------#

# Variables iniciales
fichas = 100
usuario = 0
compu = 0

print("¡Bienvenido al casino! Tu número de fichas" \
    " iniciales son", fichas, "fichas.")

#Ciclo while para repetir una y otra vez la partida hasta que el usuario quiera
while fichas > 0:
    apuesta = 0
    
    #Uso de listas:
    cartas_usuario = []
    cartas_compu = []

    while apuesta <= 0 or apuesta > fichas:
        apuesta = int((input("Ponga su apuesta:\n")))

    #Repartir cartas iniciales a la computadora
    carta_1_compu = repartir_carta()
    carta_2_compu = repartir_carta()

    cartas_compu.append(carta_1_compu)
    cartas_compu.append(carta_2_compu)

    #Repartir cartas iniciales al usuario
    carta_1_usuario = repartir_carta()
    carta_2_usuario = repartir_carta()

    cartas_usuario.append(carta_1_usuario)
    cartas_usuario.append(carta_2_usuario)

    compu = sumar_cartas(cartas_compu)
    usuario = sumar_cartas(cartas_usuario) 

    print("Dealer tiene:", [cartas_compu[0]], "=", compu - cartas_compu[1],
          "\nTienes:", cartas_usuario, "=", usuario)

    #Ciclo while que solo se repite si pide carta
    while usuario < 21:
        print("¿Qué desea hacer?\n" 
              "(1) Pedir carta\n"
              "(2) Doblar apuesta\n"
              "(3) Plantarse")

        opcion = int(input())

        if opcion == 1:
            nueva_carta = repartir_carta()
            cartas_usuario.append(nueva_carta)
            usuario = sumar_cartas(cartas_usuario)
            print("Tienes: ", cartas_usuario, "=", usuario)

        elif opcion == 2:
            if apuesta * 2 > fichas:
                print("No se puede doblar, hit")
                continue #repite el ciclo y vuelve a checar si el usuario tiene mas de 17
            apuesta = doblar_apuesta(apuesta, fichas)
            nueva_carta = repartir_carta()
            cartas_usuario.append(nueva_carta)
            usuario = sumar_cartas(cartas_usuario)
            print("Tienes: ", cartas_usuario, "=", usuario)
            break #Sale del ciclo

        elif opcion == 3:
            print("¡Buena suerte!")
            break #Sale del ciclo
        else:
            print("Opción invalida")

    while compu < 17:
        nueva_carta_compu = repartir_carta()
        cartas_compu.append(nueva_carta_compu)
        compu = sumar_cartas(cartas_compu) 
        print("El dealer roba:", nueva_carta_compu, "\n=>", cartas_compu, "=", compu)

    print("Dealer:", cartas_compu, "=", compu)
    print("Tienes:", cartas_usuario, "=", usuario)

    fichas = determinar_fichas(usuario, compu, apuesta, fichas)

    print("Fichas actuales: ", fichas)

    if fichas <= 0:
        print("Womp Womp la casa siempre gana")
        break

    seguir = input("¿Jugar otra ronda? (s/n): ")
    if seguir == "n":
        break
