import random

#Baraja
cartas = [
    ["🂡 As♠", 1], ["🂢 2♠", 2], ["🂣 3♠", 3], ["🂤 4♠", 4], ["🂥 5♠", 5], ["🂦 6♠", 6],
    ["🂧 7♠", 7], ["🂨 8♠", 8], ["🂩 9♠", 9], ["🂪 10♠", 10], ["🂫 J♠", 10], ["🂭 Q♠", 10], ["🂮 K♠", 10],

    ["🂱 As♥", 1], ["🂲 2♥", 2], ["🂳 3♥", 3], ["🂴 4♥", 4], ["🂵 5♥", 5], ["🂶 6♥", 6],
    ["🂷 7♥", 7], ["🂸 8♥", 8], ["🂹 9♥", 9], ["🂺 10♥", 10], ["🂻 J♥", 10], ["🂽 Q♥", 10], ["🂾 K♥", 10],

    ["🃁 As♦", 1], ["🃂 2♦", 2], ["🃃 3♦", 3], ["🃄 4♦", 4], ["🃅 5♦", 5], ["🃆 6♦", 6],
    ["🃇 7♦", 7], ["🃈 8♦", 8], ["🃉 9♦", 9], ["🃊 10♦", 10], ["🃋 J♦", 10], ["🃍 Q♦", 10], ["🃎 K♦", 10],

    ["🃑 As♣", 1], ["🃒 2♣", 2], ["🃓 3♣", 3], ["🃔 4♣", 4], ["🃕 5♣", 5], ["🃖 6♣", 6],
    ["🃗 7♣", 7], ["🃘 8♣", 8], ["🃙 9♣", 9], ["🃚 10♣", 10], ["🃛 J♣", 10], ["🃝 Q♣", 10], ["🃞 K♣", 10]
]


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

def main():
    # Variables iniciales
    fichas = 100
    usuario = 0
    compu = 0

    print("¡Bienvenido al casino! Tu número de fichas" \
    " iniciales son", fichas, "fichas.")

    #Ciclo while para repetir una y otra vez la partida hasta que el usuario quiera
    while fichas > 0:
        apuesta = 0
    
        #Uso de listas para valores numericos:
        cartas_compu = []
        cartas_usuario = []

        #Uso de listas para mostrar visualmente las cartas
        baraja_compu = []
        baraja_usuario = []        

        while apuesta <= 0 or apuesta > fichas:
            apuesta = int((input("Ponga su apuesta:\n")))

        #Repartir cartas iniciales a la computadora
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

        compu = sumar_cartas(cartas_compu)
        usuario = sumar_cartas(cartas_usuario) 

        print("Dealer tiene:", [baraja_compu], "=", compu - cartas_compu[1],
        "\nTienes:", baraja_usuario, "=", usuario)

        #Ciclo while que solo se repite si pide carta
        while usuario < 21:
            print("¿Qué desea hacer?\n" 
              "(1) Pedir carta\n"
              "(2) Doblar apuesta\n"
              "(3) Plantarse")

            opcion = int(input())

            if opcion == 1:
                nueva_carta = repartir_carta()
                cartas_usuario.append(nueva_carta[1])
                definir_As(cartas_usuario)
                usuario = sumar_cartas(cartas_usuario)
                print("Tienes: ", baraja_usuario, "=", usuario)

            elif opcion == 2:
                if apuesta * 2 > fichas:
                    print("No se puede doblar, hit")
                    continue #repite el ciclo y vuelve a checar si el usuario tiene mas de 17
                apuesta = doblar_apuesta(apuesta, fichas)
                nueva_carta = repartir_carta()
                cartas_usuario.append(nueva_carta[1])
                definir_As(cartas_usuario)
                usuario = sumar_cartas(cartas_usuario)
                print("Tienes: ", baraja_usuario, "=", usuario)
                break #Sale del ciclo

            elif opcion == 3:
                print("¡Buena suerte!")
                break #Sale del ciclo
            else:
                print("Opción invalida")

        while compu < 17:
            nueva_carta_compu = repartir_carta()
            cartas_compu.append(nueva_carta_compu[1])
            definir_As(cartas_compu)
            compu = sumar_cartas(cartas_compu) 
            print("El dealer roba:", nueva_carta_compu[1], "\n=>", baraja_compu, "=", compu)

        print("Dealer tiene:", baraja_compu, "=", compu)
        print("Tienes:", baraja_usuario, "=", usuario)

        fichas = determinar_fichas(usuario, compu, apuesta, fichas)

        print("Fichas actuales: ", fichas)

        if fichas <= 0:
            print("Womp Womp la casa siempre gana")
            break

        seguir = input("¿Jugar otra ronda? (s/n): ")
        if seguir == "n":
            break
main()
