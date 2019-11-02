#!/usr/bin/env python3
"""
Proyecto en Python sobre el Algoritmo de Bisección.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

import math

def fsigno(f,a,b):
    return (f(a)*f(b))


def error (actual,anterior):
    return math.fabs((actual-anterior)/actual)

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
    act=0
    ant=0
    i=1
    x=1000
    if (fsigno(f,a,b)) <0 :
        for i in range (N):
            if (x>ER):
                 ant=act
                 pmedio=(a+b)/2 
                 act=pmedio
                 if (fsigno(f,a,act)) <0:
                     b=act
                 else:
                     a=act
                 x= error(act,ant)
                 print ("Iteracion: ",i, " Punto medio: ", act, " Error: ", x)
                 i= i + 1
        return act           
    else:
        print ("No existe el intervalo")



if __name__ == "__main__":
    # Pruebe aquí su función.

    f = lambda x: 4 - x**2 -x**3

    biseccion(f, 1, 2, 0.02, 10)
    pass
