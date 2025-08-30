# Operadores aritméticos

'''
Estaba pensando en mejor hacer un sistema de apuestas donde se inicia con 100 fichas 
y el usuario escoja que apuesta hacer

Pensaba también hacer una funcion que permita doblar la mano como en blackjack
'''

# Variables iniciales
fichas = 100
apuesta = 10
usuario = 0
compu = 0
doblar = False

#Condiciones para apuesta
if apuesta <= 0:
    print("Apuesta inválida")
if apuesta > fichas:
    print("Apuesta excede fichas")

#doblar
if doblar == True:
    apuesta = apuesta * 2

# Operadores de comparación para definir resultado
if usuario > 21:
    fichas = fichas - apuesta
if compu > 21:
    fichas = fichas + apuesta
if usuario > compu:
    fichas = fichas + apuesta
if compu > usuario:
    fichas = fichas - apuesta
if usuario == compu:
    fichas = fichas
