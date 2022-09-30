# -*- coding: utf-8 -*-
from os import system, name
import random
import time
import os
from tkinter import NO

# Definición de función Clear
def Clear():
    # Windows
    if name == 'nt':
        _ = system('cls')

    # Mac - Linux
    else:
        _ = system('clear')


"""
Devuelve dos valores aleatorios:
    Palillos totales (16 a 23)
    Número de palillos a quitar (3 a 5)
"""
def sorteo_opciones(nivel):
    palillos = 1
    quitas = 0
    if nivel == 3:
        while palillos % (quitas + 1) == 0:
            palillos = random.randint(16, 23)
            quitas = random.randint(3, 5)
    else:
        palillos = random.randint(16, 23)
        quitas = random.randint(3, 5)
    return palillos, quitas


# Pantalla de inicio
def Inicio():
    print("   **************** JUEGO DE LOS PALILLOS   *************")
    print()
    print("                         1) Fácil")
    print("                         2) Difícil")
    print("                         3) Experto")
    print()
    print("   *******************************************************")
    print()
    nivel = ""
    while nivel != "1" and nivel != "2" and nivel != "3":
        nivel = input("Elige el nivel deseado (1 / 2 / 3): ")
    return nivel


# Instrucciones de juego
def Instrucciones(palillos, quitas):
    print("   **************** JUEGO DE LOS PALILLOS   *************")
    print()
    print("         I.- Habra {} palillos en total".format(palillos))
    print()
    print("         II.- Se pueden quitar entre 1 y {} palillos".format(quitas))
    print()
    print("         III.- Gana quien coge el ultimo palillo")
    print()
    print("   *******************************************************")
    print()
    print("         ¿Quién inicia el juego?")
    print()
    print("         1) Jugador")
    print("         2) Computadora")
    print()
    turno = ""
    while turno != "1" and turno != "2":
        turno = input("Elige el turno incial (1 / 2): ")
    return int(turno)


# Tablero de juego
def Tablero(palillos, quitas):
    print("   **************** JUEGO DE LOS PALILLOS   *************")
    print()
    print()

    for fila in range(4):
        print(end="   ")
        for p in range(1, palillos + 1):
            print("|", end="  ")
            if p % quitas == 0:
                print(end="\t\t")
        print()
        print()
    print("   Se pueden quitar entre 1 y {} palillos".format(quitas))
    print("   Palillos restantes: {}".format(palillos))
    print()


# Movimiento del jugador
def TurnoJugador(palillos, quitas):
    if quitas == 3:
        quitas = ("1", "2", "3")
    elif quitas == 4:
        quitas = ("1", "2", "3", "4")
    elif quitas == 5:
        quitas = ("1", "2", "3", "4", "5")
    q = input("   Palillos a quitar: ")
    while q not in quitas or int(q) > palillos:
        if q not in quitas:
            q = input("   Elige un valor entre 1 y {}: ".format(len(quitas)))
        elif int(q) > palillos:
            q = input("   Solo quedan {} palillos: ".format(palillos))
        else:
            palillos_quitar = int(q)
    return int(q)

# Turno de la computadora

# Fácil
def TurnoComputadoraFacil(palillos, quitas):
    if palillos <= quitas:
        palillos_quitar = palillos
    else:
        palillos_quitar = random.randint(1, quitas)

        while palillos_quitar > palillos:
            palillos_quitar = random.randint(1, quitas)
    print("   El ordenador retira {} de {} palillos restantes".format(
        palillos_quitar, palillos))
    input("   Presiona Enter para continuar")

    return palillos_quitar

# Difícil
def TurnoComputadorDificil(palillos, quitas):
    palillos_quitar = None

    while palillos_quitar is None or palillos_quitar > palillos:
        if palillos <= quitas:
            palillos_quitar = palillos
        elif palillos % (quitas+1) == 5:
            palillos_quitar = 5
        elif palillos % (quitas+1) == 4:
            palillos_quitar = 4
        elif palillos % (quitas+1) == 3:
            palillos_quitar = 3
        elif palillos % (quitas+1) == 2:
            palillos_quitar = 2
        elif palillos % (quitas+1) == 1:
            palillos_quitar = 1
        elif palillos % (quitas+1) == 0:
            palillos_quitar = random.randint(1, 2)
        print("   El ordenador retira {} de {} palillos restantes".format(
            palillos_quitar, palillos))
        input("   Presiona Enter para continuar")

    return palillos_quitar

# Experto
def Experto(palillos, quitas):
    palillos_quitar = None

    while palillos_quitar is None or palillos_quitar > palillos:
        if palillos <= quitas:
            palillos_quitar = palillos
        elif palillos % (quitas+1) != 0:
            palillos_quitar = palillos % (quitas+1)
        else:
            palillos_quitar = random.randint(1, 2)
        print("   El ordenador retira {} de {} palillos restantes".format(
            palillos_quitar, palillos))
        input("   Presiona Enter para continuar")

    return palillos_quitar


# Fin de la partida
def FinalPartida(turno):
    if turno == 2:
        mensaje1 = "   Has tomado el ultimo palillo"
        mensaje2 = "   *** Has ganado ***"
    elif turno == 1:
        mensaje1 = "   El ordenador toma el ultimo palillo"
        mensaje2 = "   *** Gana el ordenador ***"

    print("   **************** JUEGO DE LOS PALILLOS   *************")
    print()
    print()
    print("{}".format(mensaje1))
    print()
    print("{}".format(mensaje2))
    print()


# Función principal
def main():
    nivel = Inicio()
    Clear()

    palillos, quitas = sorteo_opciones(nivel)
    Clear()

    turno = Instrucciones(palillos, quitas)
    Clear()

    jugando = True

    while jugando:
        Tablero(palillos, quitas)

        if turno == 1:
            jugada = TurnoJugador(palillos, quitas)
            turno = 2
        elif turno == 2:
            print("   El ordenador esta pensando ...")
            time.sleep(2)
            if nivel == "1":
                jugada = TurnoComputadoraFacil(palillos, quitas)
            elif nivel == "2":
                jugada = TurnoComputadorDificil(palillos, quitas)
            elif nivel == "3":
                jugada = Experto(palillos, quitas)
            turno = 1

        palillos -= jugada
        Clear()

        if palillos == 0:
            FinalPartida(turno)
            jugando = False


main()
