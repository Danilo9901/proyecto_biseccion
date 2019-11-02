#!/usr/bin/env python3
"""
Proyecto en Python sobre el Algoritmo de Bisección.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

import math


def biseccion(a, b, ER, N, mx, m):
    err= float
    """
    Implementa el Algoritmo de Biseccion y retorna la aproximación de la raiz.

    Parámetros:
    f: función de variable real f(x).
    a: límite inferior del intervalo.
    b: límite superior del intervalo.
    ER: cota mínima del error relativo.
    N: número máximo de iteraciones.
    """
    if (n != 0):
        if (funcion(a)>0 and funcion (mx)<0):
            b= mx
        if ( funcion (a)<0 and funcion (mx) >0):
            a=a
        if (funcion (mx)>0 and funcion (b)<0 ):
            a= mx
        if ( funcion (mx)<0 and funcion (b)>0):
            b= b
        m=mx
        mx=(a+b)/2
        n=n+1
        err= (mx - m) / mx
        if (err <0):
            err=err*-1
        print("Iteración:", i, "Punto Medio:", mx, "Error:", err)
        biseccion (a, b , ER, N, mx, m)
    else:
        n=n+1
        m=(a+b)/2
        mx=m
        print("Iteración:", N, "Punto Medio:", mx, "Error: La primera iteracioón no lleva cálculo de error")
        biseccion(a,b,ER,N,mx, m)
    return mx

def funcion (a):
    return a+a

if __name__ == "__main__":
    # Pruebe aquí su función.
    b=float
    a=float    
    err= float
    print ("Algoritmo de bisección para aproximar las raices de una función.")
    print ("Ingrese los valores para los extremos A y B")
    print ("Ingrese valor de A: ")
    a= input ()
    print ("Igrese el valor de B")
    b= input ()
    print ("Ingrese el valor del error para d1etener el algoritmo")
    err= input ()
    print ("¿Cuántas veces se va a iterar si no ha llegado al error?")
    n= input()
    print (biseccion(a, b, err, n,0,0))
    pass
