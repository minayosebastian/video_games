import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)

def carrera_numerica():
    print("Bienvenido al juego de Carrera Numérica!")
    while True:
        try:
            num_jugadores = int(input("Ingrese la cantidad de jugadores (entre 2 y 4): "))
            if num_jugadores < 2 or num_jugadores > 4:
                raise ValueError("La cantidad de jugadores debe estar entre 2 y 4.")
            break
        except ValueError as e:
            print(e)
    
    clear_screen()

    while True:
        print("Niveles de tablero:")
        print("1. Nivel básico (Tablero de 20 posiciones)")
        print("2. Nivel intermedio (Tablero de 30 posiciones)")
        print("3. Nivel avanzado (Tablero de 50 posiciones)")
        print("4. Nivel experto (Tablero de 100 posiciones)")
        nivel = input("Seleccione el nivel de tablero a jugar: ")
        if nivel in ['1', '2', '3', '4']:
            if nivel == '1':
                meta = 20
            elif nivel == '2':
                meta = 30
            elif nivel == '3':
                meta = 50
            else:
                meta = 100
            break
        else:
            print("Por favor, ingrese una opción válida.")
    
    clear_screen()

    posiciones = [0] * num_jugadores
    pares_consecutivos = [0] * num_jugadores

    while True:
        for jugador in range(num_jugadores):
            input(f"\nTurno del jugador {jugador + 1}. Presione Enter para lanzar los dados...")
            dado1, dado2 = lanzar_dados()
            total = dado1 + dado2
            nueva_posicion = posiciones[jugador] + total
            posiciones[jugador] = nueva_posicion
            print(f"Jugador {jugador + 1}: Has sacado un {dado1} y un {dado2}. Avanzas {total} casillas. Ahora estás en la posición {posiciones[jugador]}")

            if dado1 == dado2:
                pares_consecutivos[jugador] += 1
                if pares_consecutivos[jugador] == 3:
                    print(f"¡Jugador {jugador + 1} ha obtenido 3 pares consecutivos! ¡Ha ganado!")
                    return

            if nueva_posicion >= meta:
                print(f"¡Jugador {jugador + 1} ha llegado a la meta y ha ganado!")
                return

carrera_numerica()
