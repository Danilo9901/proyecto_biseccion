#!/usr/bin/env python3
"""
Proyecto en Python sobre el Algoritmo de Bisección.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""
import math
def biseccion(f, a, b, ER, N):
    """
        Implementa el Algoritmo de Biseccion y retorna la aproximación de la raiz.
        Parámetros:
        f: función de variable real f(x).
        a: límite inferior del intervalo.
        b: límite superior del intervalo.
        ER: cota mínima del error relativo.
        N: número máximo de iteraciones.
    """
    Ea=100 #Error relativo actual
    r_Superior=0 #Rango superior
    r_Inferior=0 #Rango inferior
    i=1 #Numero de Iteraciones Realizadas
    if( (f(a) * f(b) > 0) | N<0): #Reemplazo del manejo de excepcion
        raise Exception("Los datos ingresados no cumplen los requisitos.")
    while ( (N>i) & (Ea>ER) ): #Se comprueba que no exceda el numero de iteraciones y que el error relativo no ha alcanzado el punto deseado
        r_Inferior = r_Superior #Se asignan rangos
        r_Superior = ( ( a + b )/2)
        if ( ( f( r_Superior) * f(b) ) < 0): #Se comprueba el rango para asignar el intervalo inferior y superior
            a= r_Superior
        else: 
            b= r_Superior 
        if (i>1):
            Ea=abs( ( ( r_Superior - r_Inferior) /  r_Superior) * 100 ) #Se calcula el error absoluto actual 
            print("Iteración:", i, "Punto Medio:",  r_Superior, "Error:", Ea)
        else: print("Iteración:", i, "Punto Medio:",  r_Superior)
        i+=1  
    return r_Superior
f1 = lambda x:math.exp(x) - ( 3 * pow(x,2)) #Funcion hecha en clase con los puntos 0 y 1
f2 = lambda x: pow(x,3) + (4 * pow(x,2)) - 10 #Funcion con punto 1 y 2

if __name__ == "__main__":
    a=biseccion( f1, 0, 1, 3, -15)