#!/usr/bin/env python3
"""
Proyecto en Python sobre el Algoritmo de Bisección.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

import math
'''Metodo anonima que contiene la ecuacion'''
fn = lambda x: math.e**x - 3*(x**2)

'''Metodo que verifica si los intervalos pertenecen
   a signos opuestos'''
def verificarFuncion(fn,x,y):                      
    return True if (fn(x) * fn(y) < 0) else False

'''Metodo que verifica si los intervalos pertenecen
   a signos opuestos'''
def errorRelativo(pm_actual, pm_anterior):
    return abs((pm_actual - pm_anterior) / pm_actual)

def biseccion(fn, a, b, ER, N):
    """
    Implementa el Algoritmo de Biseccion y retorna la aproximación de la raiz.

    Parámetros:
    f: función de variable real f(x).
    a: límite inferior del intervalo.
    b: límite superior del intervalo.
    ER: cota mínima del error relativo.
    N: número máximo de iteraciones.
    """
    try:
        if (verificarFuncion(fn,a,b)):
            pm_actual = 0
            for iteracion in range(N):
                pm_anterior = pm_actual
                pm_actual = (a + b) / 2.0
            
                if pm_actual * fn(b): a = pm_actual
                else: b = pm_actual
            
                if errorRelativo(pm_actual,pm_anterior) <= ER: return pm_actual 
                print("Iteración:", iteracion, "Punto Medio:", pm_actual, "Error: ", errorRelativo(pm_actual,pm_anterior))   
    except ValueError:
        print ('La funcion no cumple con los requisitos.')
    return pm_actual


if __name__ == "__main__":
    print (biseccion(fn,0,1,0.02,10))