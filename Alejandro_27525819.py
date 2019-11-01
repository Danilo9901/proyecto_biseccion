#!/usr/bin/env python3
"""
Proyecto en Python sobre el Algoritmo de Bisección.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

import math

def f(x):
    return math.log(x)+x**2-4

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
    rela=100
    v_actu=0
    v_prev=0
    ni=1 
    while(ER<rela) and (ni<N):
        v_actu=(a+b)/2
        ra=f(a)
        rv=f(v_actu)
        result=ra*rv
        if result > 0:
            a=v_actu
        else:
            b=v_actu
        rela=abs(v_actu-v_prev)/v_actu
        v_prev=v_actu    
        print("Iteración:", ni, "Punto Medio:", v_actu, "Error:", rela)
        ni=ni+1

    return v_actu


if __name__ == "__main__":
    # Pruebe aquí su función.
    print (biseccion(f,1,2,0.01,10))
    pass
