# BLACKJACK
Diego Hernández Rangel - A01710524

El programa de BlackJack es una simulación del clásico juego de cartas de casino. En este juego, el objetivo del usuario es conseguir una mano con un valor lo más cercano posible a 21 sin pasarse, compitiendo contra la computadora (dealer).
El usuario comienza con una cantidad inicial de fichas y podrá decidir en cada ronda cuánto apostar. Las reglas básicas del BlackJack aplican, con tres acciones disponibles:

&nbsp;-Pedir carta (solicitar una carta nueva)

&nbsp;-Plantarse (mantener su mano actual)

&nbsp;-Doblar apuesta (duplicar la apuesta y recibir una última carta)

El juego continúa hasta que el jugador se quede sin fichas o decida retirarse.

### Algoritmo
El programa sigue una estructura basada en funciones, donde se combinan condicionales, ciclos y listas para simular la dinámica del BlackJack.

1 Inicialización: El jugador comienza con 100 fichas.

2 Apuesta: Se valida que la apuesta sea válida (no puede ser menor o igual a 0 ni mayor al número de fichas disponibles).

3 Repartición inicial: El usuario y el dealer reciben dos cartas al azar desde una baraja estándar de 52 cartas. El jugador solo puede ver una carta del dealer hasta que termine su turno.

4 Turno del jugador: El jugador elige entre pedir carta, plantarse o doblar la apuesta.

&nbsp;-Si pide carta, recibe una nueva y se actualiza el valor total.

&nbsp;-Si se pasa de 21, pierde automáticamente la ronda.

&nbsp;-Si dobla, se duplica la apuesta y se recibe una carta más (solamente disponible en el primer turno).

5 Se repite el turno del jugador hasta que este decida plantarse o se pase de 21.

6 Turno del dealer: La computadora pedirá cartas automáticamente hasta alcanzar un valor mínimo de 17.

7 Determinación del resultado: Se comparan las manos para determinar si el jugador gana, pierde o empata. Las fichas se ajustan de acuerdo con el resultado.

8 Continuación del juego: El jugador puede decidir si desea jugar otra ronda o retirarse.

### Pseudocódigo

``` 
inicializar fichas = 100
mientras fichas > 0 y jugador quiera seguir:
 apuesta = solicitar cantidad válida
 repartir 2 cartas al jugador
 repartir 2 cartas al dealer
 mostrar cartas iniciales del jugador y una del dealer

 turno del jugador:
 mientras el valor de la mano del jugador < 21:
  si primer turno:
   mostrar opciones (pedir, plantarse, doblar)
  sino:
   mostrar opciones (pedir, plantarse)
  leer opción
  si opción = pedir:
   dar nueva carta
   actualizar valor
  si opción = doblar y primer turno:
   duplicar apuesta si no se pasa
   dar una carta
   terminar turno
  si opción = plantarse:
   terminar turno

 turno del dealer:
 mientras el valor de la mano del dealer < 17:
  dealer roba carta
  actualizar valor

 resultado:
 si jugador > 21 → pierde
 si dealer > 21 → gana jugador
 si jugador > dealer → gana jugador
 si dealer > jugador → pierde jugador
 si empate → nadie gana
 ajustar fichas según resultado
 mostrar fichas actuales

 si fichas <= 0:
  mostrar "la casa gana"
 preguntar si desea jugar otra ronda
```

### Bibliotecas usadas

El programa usa solo bibliotecas estándar de Python, por lo que no requiere instalación adicional:

&nbsp;-random: para seleccionar cartas al azar desde la baraja, simulando el reparto real. Se utiliza random.randint(rango), el cual selecciona un numero entero dentro del rango utilizado

&nbsp;-time: para agregar pausas (time.sleep(segundos)) y hacer que el juego se sienta más fluido y natural, especialmente durante el turno del dealer.

### Instrucciones

Para jugarlo, descarga o copia el código en un archivo con nombre y luego ejecuta el programa en tu terminal o IDE favorito. Ahora solo sigue las instrucciones en pantalla:

&nbsp;-Ingresa tu apuesta.

&nbsp;-Usa los números 1, 2, o 3 para elegir entre Pedir carta, Plantarte o Doblar apuesta.

&nbsp;-Observa los resultados de cada ronda y decide si deseas seguir jugando.

Disfruta!!!
