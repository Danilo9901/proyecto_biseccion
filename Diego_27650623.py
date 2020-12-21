#!/usr/bin/env python3
"""
Proyecto en Python sobre el Algoritmo de Bisección.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

import math


def biseccion(f, a, b, ER, N):
    """
    Implementa el Algoritmo de Biseccion y retorna la aproximación.

    Parámetros:
    f: función de variable real f(x).
    a: límite inferior del intervalo.
    b: límite superior del intervalo.
    ER: cota mínima del error relativo.
    N: número máximo de iteraciones.
    """
    
    i=0; pm_actual=0; pm_anterior=0; err=ER+1
    if (f(a)*f(b))>0:
        print ("No se cumple el teorema del valor intermedio") 
    else:       
        while (err>ER) and (i<N):        
            pm_actual=(a+b)/2.0
            if (f(a)*f(pm_actual))>0:
                a=pm_actual
            else:
                b=pm_actual                    
            if(i==0):
                print("Iteración:", i+1, "Punto Medio:", pm_actual, "Error: ------------------------") 
            else:
                err= abs((pm_actual-pm_anterior)/pm_actual)
                print("Iteración:", i+1, "Punto Medio:", pm_actual, "Error:", err)
            pm_anterior=pm_actual
            i=i+1  
    return pm_actual


if __name__ == "__main__":
    # Pruebe aquí su función. ----- se utilizo el ejemplo 1 de la clase 
    f = lambda x: math.exp(x)-3*x**2
    biseccion(f,0,1,0.03,40)
   
    pass
