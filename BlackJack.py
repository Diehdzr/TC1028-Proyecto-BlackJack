'''
Estaba pensando en mejor hacer un sistema de apuestas donde se inicia con 100 fichas 
y el usuario escoja que apuesta hacer

Pensaba también hacer una funcion que permita doblar la mano como en blackjack
'''

#Posiblemente me este adelantando, pero ya conocia que existia
# esta biblioteca, entonces la investigue
#un poco para añadirla a una pequeña función

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

while fichas > 0:
    apuesta = 0
    while apuesta <= 0 or apuesta > fichas:
        apuesta = int((input("Ponga su apuesta:\n")))

    carta_1_compu = repartir_carta()
    carta_2_compu = repartir_carta()
    compu = carta_1_compu + carta_2_compu

    carta_1_usuario = repartir_carta()
    carta_2_usuario = repartir_carta()
    usuario = carta_1_usuario + carta_2_usuario

    print("Dealer tiene: ", carta_1_compu, "\nTienes: ", 
          carta_1_usuario, carta_2_usuario)

    while usuario < 21:
        print("¿Qué desea hacer?\n" 
              "(1) Pedir carta\n"
              "(2) Doblar apuesta\n"
              "(3) Plantarse")

        opcion = int(input())

        if opcion == 1:
            nueva_carta = repartir_carta()
            print("Tienes: ", usuario, "+", nueva_carta)
            usuario = usuario + nueva_carta
        elif opcion == 2:
            if apuesta * 2 > fichas:
                print("No se puede doblar, hit")
                continue
            apuesta = doblar_apuesta(apuesta, fichas)
            nueva_carta = repartir_carta()
            print("Tienes: ", usuario, "+", nueva_carta)
            usuario = usuario + nueva_carta
            break
        elif opcion == 3:
            print("¡Buena suerte!")
            break
        else:
            print("Opción invalida")

    while compu < 17:
        nueva_carta_compu = repartir_carta()
        compu = compu + nueva_carta_compu 
        print("El dealer roba:", nueva_carta_compu, "=>", compu)

    print("Dealer:", compu)
    print("Tienes:", usuario)

    fichas = determinar_fichas(usuario, compu, apuesta, fichas)

    print("Fichas actuales: ", fichas)

    if fichas <= 0:
        print("Womp Womp la casa siempre gana")
        break

    seguir = input("¿Jugar otra ronda? (s/n): ")
    if seguir == "n":
        break
