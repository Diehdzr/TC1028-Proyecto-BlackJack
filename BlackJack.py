import random
import time

#Baraja
cartas = [
    ["🂡 As♠", 11], ["🂢 2♠", 2], ["🂣 3♠", 3], ["🂤 4♠", 4], ["🂥 5♠", 5], ["🂦 6♠", 6],
    ["🂧 7♠", 7], ["🂨 8♠", 8], ["🂩 9♠", 9], ["🂪 10♠", 10], ["🂫 J♠", 10], ["🂭 Q♠", 10], ["🂮 K♠", 10],

    ["🂱 As♥", 11], ["🂲 2♥", 2], ["🂳 3♥", 3], ["🂴 4♥", 4], ["🂵 5♥", 5], ["🂶 6♥", 6],
    ["🂷 7♥", 7], ["🂸 8♥", 8], ["🂹 9♥", 9], ["🂺 10♥", 10], ["🂻 J♥", 10], ["🂽 Q♥", 10], ["🂾 K♥", 10],

    ["🃁 As♦", 11], ["🃂 2♦", 2], ["🃃 3♦", 3], ["🃄 4♦", 4], ["🃅 5♦", 5], ["🃆 6♦", 6],
    ["🃇 7♦", 7], ["🃈 8♦", 8], ["🃉 9♦", 9], ["🃊 10♦", 10], ["🃋 J♦", 10], ["🃍 Q♦", 10], ["🃎 K♦", 10],

    ["🃑 As♣", 11], ["🃒 2♣", 2], ["🃓 3♣", 3], ["🃔 4♣", 4], ["🃕 5♣", 5], ["🃖 6♣", 6],
    ["🃗 7♣", 7], ["🃘 8♣", 8], ["🃙 9♣", 9], ["🃚 10♣", 10], ["🃛 J♣", 10], ["🃝 Q♣", 10], ["🃞 K♣", 10]
]


#FUNCIONES BÁSICAS Y DE OPERADORES
def poner_apuesta(fichas, apuesta):
    if apuesta <= 0:
        return "Apuesta invalida"
    elif apuesta > fichas:
        return "Apuesta excede fichas"
    return apuesta

def doblar_apuesta(apuesta, fichas):
    if apuesta * 2 > fichas:
        print("Apuesta demasiado grande, se mantiene apuesta actual")
        return apuesta
    return apuesta * 2


#Funcion para contar las cartas
def sumar_cartas(cartas):
    sum = 0
    for n in cartas:
        sum = sum + n
    return sum


def definir_As(cartas):
    i = 0
    while i < len(cartas):
        if sumar_cartas(cartas) > 21 and cartas[i] == 11:
            cartas[i] = 1
        i += 1

#como mencione, use la biblioteca de random para hacer esta función
#docs.python.org/es/3.10/library/random.html
#La función obtiene la posición de forma aleatoria de la matriz
def obtener_posicion():
    tam_cartas = len(cartas) - 1
    carta_posicion = random.randint(0, tam_cartas)
    return carta_posicion

#Obtenemos el valor de la carta a partir de su posición
def repartir_carta():
    pos = obtener_posicion()
    return cartas[pos]

# Operadores de comparación para definir resultado

def determinar_fichas(usuario, compu, apuesta, fichas):
    if usuario > 21:
        fichas = fichas - apuesta
        print("Te pasaste!")
    elif compu > 21:
        fichas = fichas + apuesta
        print("El dealer se pasó!")
    elif usuario > compu:
        fichas = fichas + apuesta
        print("Ganaste!")
    elif compu > usuario:
        fichas = fichas - apuesta
        print("Perdiste!")
    elif usuario == compu:
        fichas = fichas
        print("Empate!")

    return fichas


#FUNCIONES PARA EL JUEGO

def inicializar_juego():
    fichas = 100
    print("¡Bienvenido al casino! Tu número de fichas" \
    " iniciales son", fichas, "fichas.")
    return fichas

def poner_apuesta(fichas, apuesta):
    while apuesta <= 0 or apuesta > fichas:
            apuesta = int((input("Ponga su apuesta:\n")))
    return apuesta    

#Repartir cartas iniciales a la computadora
def repartir_cartas_iniciles(cartas_compu, baraja_compu, cartas_usuario, baraja_usuario):
    carta_1_compu = repartir_carta()
    carta_2_compu = repartir_carta()

    #Añadir valores
    cartas_compu.append(carta_1_compu[1])
    cartas_compu.append(carta_2_compu[1])

    #Añadir visuales
    baraja_compu.append(carta_1_compu[0])
    baraja_compu.append(carta_2_compu[0])

    #Repartir cartas iniciales al usuario
    carta_1_usuario = repartir_carta()
    carta_2_usuario = repartir_carta()

    #Añadir valores
    cartas_usuario.append(carta_1_usuario[1])
    cartas_usuario.append(carta_2_usuario[1])

    #Añadir visuales
    baraja_usuario.append(carta_1_usuario[0])
    baraja_usuario.append(carta_2_usuario[0])

    #Definir As
    definir_As(cartas_usuario)
    definir_As(cartas_compu)

def nuevas_cartas_usuario(cartas_usuario, baraja_usuario):
    nueva_carta = repartir_carta()
    cartas_usuario.append(nueva_carta[1])
    baraja_usuario.append(nueva_carta[0])
    definir_As(cartas_usuario)

def turno_jugador(cartas_usuario, baraja_usuario, usuario, fichas, apuesta):
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
            nuevas_cartas_usuario(cartas_usuario, baraja_usuario)
            usuario = sumar_cartas(cartas_usuario)
            print("Tienes: ", baraja_usuario, "=", usuario, "\n")
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


def turno_compu(cartas_compu, baraja_compu, compu):
    while compu < 17:
            nueva_carta = repartir_carta()
            cartas_compu.append(nueva_carta[1])
            baraja_compu.append(nueva_carta[0])
            definir_As(cartas_compu)
            compu = sumar_cartas(cartas_compu) 
            print("El dealer roba:", nueva_carta[1], "\n=>", baraja_compu, "=", compu, "\n")
            time.sleep(1)
    return compu

#----------Programa principal -------------#

def main():
    # Variables iniciales
    fichas = inicializar_juego()
    usuario = 0
    compu = 0

    #Ciclo while para repetir una y otra vez la partida hasta que el usuario quiera
    while fichas > 0:
        apuesta = 0
    
        #Uso de listas para valores numericos:
        cartas_compu = []
        cartas_usuario = []
        #Uso de listas para mostrar visualmente las cartas
        baraja_compu = []
        baraja_usuario = []        

        apuesta = poner_apuesta(fichas, apuesta)

        repartir_cartas_iniciles(cartas_compu, baraja_compu, cartas_usuario, baraja_usuario)
        
        compu = sumar_cartas(cartas_compu)
        usuario = sumar_cartas(cartas_usuario) 

        print("Dealer tiene:", [baraja_compu[0]], "=", cartas_compu[0],
        "\nTienes:", baraja_usuario, "=", usuario)

        usuario, apuesta = turno_jugador(cartas_usuario, baraja_usuario, usuario, fichas, apuesta)
        if usuario <= 21:
            print("Turno del dealer")
            time.sleep(1.5)
            compu = turno_compu(cartas_compu, baraja_compu, compu)
            print("Dealer tiene:", baraja_compu, "=", compu)
            print("Tienes:", baraja_usuario, "=", usuario, "\n")
            
        time.sleep(1.5)

        fichas = determinar_fichas(usuario, compu, apuesta, fichas)

        print("Fichas actuales: ", fichas)

        if fichas <= 0:
            print("Womp Womp la casa siempre gana")
            break

        seguir = input("¿Jugar otra ronda? (s/n): ")
        if seguir == "n":
            break
main()
