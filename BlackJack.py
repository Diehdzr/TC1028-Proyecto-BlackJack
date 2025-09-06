'''
Estaba pensando en mejor hacer un sistema de apuestas donde se inicia con 100 fichas 
y el usuario escoja que apuesta hacer

Pensaba también hacer una funcion que permita doblar la mano como en blackjack
'''

#Posiblemente me este adelantando, pero ya conocia que existia esta biblioteca, entonces la investigue
#un poco para añadirla a una pequeña función

import random

# Variables iniciales
fichas = 100
apuesta = 10
usuario = 0
compu = 0

#FUNCIONES BÁSICAS

def poner_apuesta(fichas, apuesta):
    if apuesta <= 0:
        return "Apuesta invalida"
    elif apuesta > fichas:
        return "Apuesta excede fichas"
    else:
        return apuesta

def doblar_apuesta(apuesta, fichas):
    if apuesta * 2 > fichas:
        return apuesta
    else:
        return apuesta * 2
    
#como mencione, use la biblioteca de random para hacer esta función
#docs.python.org/es/3.10/library/random.html
def repartir_carta():
    return random.randint(1,11)

# Operadores de comparación para definir resultado

def determinar_resultado(usuario, compu, apuesta, fichas):
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

#prueba de la biblioteca
print(repartir_carta())
