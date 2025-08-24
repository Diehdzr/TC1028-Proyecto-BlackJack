# BLACKJACK-
Diego Hernández Rangel - A01710524
Este es mi proyecto libre final de TC 1028. Mi idea es hacer una simulación de blackjack (21), donde la computadora escoge aleatoriamente cartas del 1 al 11, pero con el 10 teniendo más probabilidad de aparecer para representar las cartas de Jack, Queen y King. La dinámica es que ambos jugadores empiezan con 2 cartas, pero el jugador solo puede ver una de las cartas de la computadora (que funciona como la mesa). A partir de ahí, el jugador decide si quiere pedir más cartas las veces que quiera, mientras que la computadora debe seguir pidiendo cartas siempre que tenga menos de 17 puntos.
El jugador empieza con 0 puntos y gana uno cuando gana una ronda o pierde uno cuando gana la computadora. El juego acaba cuando el jugador lo decida mostrando su "high-score".
Elegí este proyecto porque me interesa mucho aprender a programar videojuegos en el futuro, y considero que esta es una idea sencilla que me permite practicar conceptos básicos de programación dentro de una temática que me motiva.

Pseudocódigo:

variables iniciales:
puntos_usuario
puntos_compu
puntos

hit_carta()
  carta = escoger_random(1, 11)
 
  regresar carta

turno_usuario():
    suma = 0
        nueva = hit_carta()
        suma = suma + nueva
        imprimir "Carta:", nueva, " Total:", suma
        SI suma >= 21:
            acabar función
        decision = PEDIR "¿Otra carta? (s/n): "
        SI decision == "n":
            acabar función
    regresar suma

turno_compu():
    suma = 0
    MIENTRAS suma < 17:
        nueva = hit_carta()
        suma = suma + nueva
    imprimir "Total computadora:", suma
    regresar suma
    
jugar_ronda():

  SI usuario > 21:
        imprimir "Usuario se pasó. Punto para compu."
        puntos = puntos - 1
  SI NO, SI compu > 21:
        imprimir "Compu se pasó. Punto para usuario."
        puntos = puntos + 1
  SI NO, SI usuario > compu:
        imprimir "Usuario gana la ronda."
        puntos = puntos + 1
  SI NO, SI compu > usuario:
        imprimir "Compu gana la ronda."
        puntos = puntos - 1
  SI NO:
        IMPRIMIR "Empate."
        puntos = puntos
  regresar puntos

------------------PROGRAMA PRINCIPAL----------------------

pedir al jugador si quiere jugar otra ronda (s/n)
MIENTRAS s
    jugar_ronda():
    IMPRIMIR "Puntos acumulados:", puntos
    pedir al usuario si quiere jugar otra ronda (s/n)

imprimir "Juego terminado. Puntos finales:", puntos
