"""
Proyecto final
Programa para simular el juego de cartas BlackJack
En este programa las reglas basicas del BlackJack aplican, pero solo se le
permite al jugador hacer tres acciones: Pedir carta, plantarse o doblar
"""

#Bibliotecas
import random
import time

#========================= funciones auxiliares ===============================

def poner_apuesta(fichas, apuesta):
    """
    (Uso de condicionales)
    Verificar que la apuesta que se va a poner no exceda la
    cantidad de fichas. Si no excede regresa la apuesta
    """
    if apuesta <= 0:
        return "Apuesta invalida"
    elif apuesta > fichas:
        return "Apuesta excede fichas"
    return apuesta


def doblar_apuesta(apuesta, fichas):
    """
    (Uso de condicionales)
    Verificar si al doblar la apuesta no exceder la cantidad de fichas que 
    tiene. En caso de que se exceda se mantiene la apuesta inicial
    """
    if apuesta * 2 > fichas:
        print("Apuesta demasiado grande, se mantiene apuesta actual")
        return apuesta
    return apuesta * 2


def sumar_cartas(cartas):
    """
    (Uso de ciclo for y operadores)
    Calcular el valor de una mano. Se toman las cartas como
    elementos de una lista, por lo que la funcion solo cuenta el valor total
    de la lista.
    """
    sum = 0
    for n in cartas:
        sum = sum + n
    return sum


def definir_As(cartas):
    """
    (Uso de ciclos while, listas y condicionales)
    En BlackJack el As cuenta como 11, al menos que la mano se pase de 21,
    entonces cuenta como 1. Esta funcion calcula si es necesario cambiar el As
    a 1
    """
    i = 0
    while i < len(cartas):
        if sumar_cartas(cartas) > 21 and cartas[i] == 11:
            cartas[i] = 1
        i += 1


def obtener_posicion(cartas):
    """
    (Uso de biblioteca)
    De forma aleatoria se escoge el indice de la carta que se va a repartir
    """
    tam_cartas = len(cartas) - 1
    carta_posicion = random.randint(0, tam_cartas)
    return carta_posicion

def repartir_carta(cartas):
    """
    (Uso de funciones y listas anidadas)
    Obtener la carta con el indice obtenido de la funcion obtener_posicion
    """
    pos = obtener_posicion(cartas)
    return cartas[pos]

def determinar_fichas(usuario, compu, apuesta, fichas):
    """
    (Uso de condicionales, operadores)
    A partir del valor de la mano de cada jugador se calcula cuantas fichas
    gana o pierde el usuario
    """
    if usuario > 21:
        fichas = fichas - apuesta
        print("Te pasaste!\n")
    elif compu > 21:
        fichas = fichas + apuesta
        print("El dealer se pasó!\n")
    elif usuario > compu:
        fichas = fichas + apuesta
        print("Ganaste!\n")
    elif compu > usuario:
        fichas = fichas - apuesta
        print("Perdiste!\n")
    elif usuario == compu:
        fichas = fichas
        print("Empate!\n")

    return fichas


#========================= funciones principales ==============================

def inicializar_juego():
    """
    (Uso de variables)
    Se inicializan las fichas con las que empieza el jugador
    """
    fichas = 100
    print("¡Bienvenido al casino! Tu número de fichas" \
    " iniciales son", fichas, "fichas.")
    return fichas

def poner_apuesta(fichas, apuesta):
    """
    (Condicionales)
    Verificar si al poner la apuesta se hace una apuesta valida
    """
    while apuesta <= 0 or apuesta > fichas:
            apuesta = int((input("Ponga su apuesta:\n")))
    return apuesta    

def repartir_cartas_iniciles(cartas_compu, baraja_compu, cartas_usuario, 
    baraja_usuario, cartas):
    """
    (Uso de funciones y listas anidadas)
    Recibe: una lista que presenta la carta visual y otra que contiene su valor
    Se agregan de forma aleatoria las cartas iniciales (2 para el usuario y 2 
    para la computadora)
    """
    carta_1_compu = repartir_carta(cartas)
    carta_2_compu = repartir_carta(cartas)

    #Añadir valores
    cartas_compu.append(carta_1_compu[1])
    cartas_compu.append(carta_2_compu[1])

    #Añadir visuales
    baraja_compu.append(carta_1_compu[0])
    baraja_compu.append(carta_2_compu[0])

    #Repartir cartas iniciales al usuario
    carta_1_usuario = repartir_carta(cartas)
    carta_2_usuario = repartir_carta(cartas)

    #Añadir valores
    cartas_usuario.append(carta_1_usuario[1])
    cartas_usuario.append(carta_2_usuario[1])

    #Añadir visuales
    baraja_usuario.append(carta_1_usuario[0])
    baraja_usuario.append(carta_2_usuario[0])

    #Definir As
    definir_As(cartas_usuario)
    definir_As(cartas_compu)

def nuevas_cartas_usuario(cartas_usuario, baraja_usuario, cartas):
    """
    (Uso de funciones y listas anidadas)
    Repartir una carta nueva y repartir su valor y visual en la lista
    correspondiente
    """
    nueva_carta = repartir_carta(cartas)
    cartas_usuario.append(nueva_carta[1])
    baraja_usuario.append(nueva_carta[0])
    definir_As(cartas_usuario)

def turno_jugador(cartas_usuario, baraja_usuario, usuario, fichas, apuesta):
    """
    (Uso de funciones, condicionales anidados, ciclos while, listas anidadas)
    Se le da 3 opciones al usuario, pedir carta, plantarse o doblar (solamente
    en el primer turno) Y repite hasta que el jugador decida plantarse o se
    pase de 21
    """
    primer_turno = True
    while usuario < 21:
        if primer_turno == True:
            print("¿Qué desea hacer?\n" 
                  "(1) Pedir carta\n"
                  "(2) Plantarse\n"
                  "(3) Doblar apuesta")
        else:
            print("¿Qué desea hacer?\n" 
                  "(1) Pedir carta\n"
                  "(2) Plantarse")

        opcion = int(input())

        if opcion == 1:
            nuevas_cartas_usuario(cartas_usuario, baraja_usuario, cartas)
            usuario = sumar_cartas(cartas_usuario)
            print("Tienes: ", baraja_usuario, "=", usuario)
            primer_turno = False

        elif opcion == 2:
            print("¡Buena suerte!")
            break #Sale del ciclo

        elif opcion == 3:
            if primer_turno == True:
                apuesta = doblar_apuesta(apuesta, fichas)
                nuevas_cartas_usuario(cartas_usuario, baraja_usuario)
                usuario = sumar_cartas(cartas_usuario)
                print("Tienes: ", baraja_usuario, "=", usuario, "\n")
                break #Sale del ciclo
            else:
                print("Opción inválida, no es el primer turno")

        else:
            print("Opción invalida")
    return usuario, apuesta


def turno_compu(cartas_compu, baraja_compu, compu, cartas):
    """
    (Uso de funciones, biblioteca, condicionales anidados, ciclos while, l
    istas anidadas)
    La computadora pide carta una y otra vez hasta que consiga minimo 17. 
    Utilizar sleep para que sea mas fluido y no tan repentino el print
    """
    while compu < 17:
            nueva_carta = repartir_carta(cartas)
            cartas_compu.append(nueva_carta[1])
            baraja_compu.append(nueva_carta[0])
            definir_As(cartas_compu)
            compu = sumar_cartas(cartas_compu) 
            print("El dealer roba:", nueva_carta[1], "\n=>", baraja_compu, 
            "=", compu, "\n")
            time.sleep(1)
    return compu

#========================= programa principal =================================

#Baraja
cartas = [
    ["🂡 As♠", 11], ["🂢 2♠", 2], ["🂣 3♠", 3], ["🂤 4♠", 4], ["🂥 5♠", 5], 
    ["🂦 6♠", 6], ["🂧 7♠", 7], ["🂨 8♠", 8], ["🂩 9♠", 9], ["🂪 10♠", 10], 
    ["🂫 J♠", 10], ["🂭 Q♠", 10], ["🂮 K♠", 10],

    ["🂱 As♥", 11], ["🂲 2♥", 2], ["🂳 3♥", 3], ["🂴 4♥", 4], ["🂵 5♥", 5], 
    ["🂶 6♥", 6], ["🂷 7♥", 7], ["🂸 8♥", 8], ["🂹 9♥", 9], ["🂺 10♥", 10], 
    ["🂻 J♥", 10], ["🂽 Q♥", 10], ["🂾 K♥", 10],

    ["🃁 As♦", 11], ["🃂 2♦", 2], ["🃃 3♦", 3], ["🃄 4♦", 4], ["🃅 5♦", 5], 
    ["🃆 6♦", 6], ["🃇 7♦", 7], ["🃈 8♦", 8], ["🃉 9♦", 9], ["🃊 10♦", 10], 
    ["🃋 J♦", 10], ["🃍 Q♦", 10], ["🃎 K♦", 10],

    ["🃑 As♣", 11], ["🃒 2♣", 2], ["🃓 3♣", 3], ["🃔 4♣", 4], ["🃕 5♣", 5], 
    ["🃖 6♣", 6], ["🃗 7♣", 7], ["🃘 8♣", 8], ["🃙 9♣", 9], ["🃚 10♣", 10], 
    ["🃛 J♣", 10], ["🃝 Q♣", 10], ["🃞 K♣", 10]
]

def main():
    """
    En esta función se combina todas las funciones ya hechas para que el juego
    tenga una estructura
    """
    # Variables iniciales
    fichas = inicializar_juego()
    usuario = 0
    compu = 0
    
    #Bandera para decidir si el jugador quiere seguir jugando
    bandera = False

    #Ciclo while para repetir una y otra vez la partida
    while fichas > 0 and bandera == False:
        apuesta = 0
    
        #Uso de listas para valores numericos:
        cartas_compu = []
        cartas_usuario = []
        #Uso de listas para mostrar visualmente las cartas
        baraja_compu = []
        baraja_usuario = []        

        apuesta = poner_apuesta(fichas, apuesta)

        repartir_cartas_iniciles(cartas_compu, baraja_compu, cartas_usuario, 
        baraja_usuario, cartas)
        
        compu = sumar_cartas(cartas_compu)
        usuario = sumar_cartas(cartas_usuario) 

        print("Dealer se planta:", [baraja_compu[0]], "=", cartas_compu[0],
        "\nTienes:", baraja_usuario, "=", usuario)

        usuario, apuesta = turno_jugador(cartas_usuario, baraja_usuario, 
        usuario, fichas, apuesta)
        if usuario <= 21:
            print("Turno del dealer")
            time.sleep(1.5)
            compu = turno_compu(cartas_compu, baraja_compu, compu, cartas)
            print("Dealer tiene:", baraja_compu, "=", compu)
            print("Tienes:", baraja_usuario, "=", usuario, "\n")
            
        time.sleep(1.5)

        fichas = determinar_fichas(usuario, compu, apuesta, fichas)

        print("Fichas actuales: ", fichas)

        if fichas <= 0:
            print("Womp Womp la casa siempre gana")

        seguir = input("¿Jugar otra ronda? (s/n): ")
        if seguir == "n":
            bandera = True
main()
