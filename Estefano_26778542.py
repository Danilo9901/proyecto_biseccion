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
    err=100     #Error relativo aproximado 
    i=1        #Contador de iteraciones
    m_Act=0     #Punto medio actual
    m_Ant=0     #punto medio anterior

    if(f(a)*f(b)<0):

        while (err>ER) and (i<N):

            m_Ant = m_Act
            m_Act = (a + b)/2

            if (f(m_Act) * f(a) < 0):
                b = m_Act    
            else:
                a = m_Act
            
            if(i > 1):
                err=abs((m_Act-m_Ant)/m_Act)

            print("Iteración:", i, "Punto Medio:", m_Act, "Error:", err)

            i+=1   
                   
    else:
        print("Esta funcón o los puntos a y b, no cumple con el teorema del valor intermedio")

    return m_Act


if __name__ == "__main__":
    # Pruebe aquí su función.
    f = lambda x: math.e**x - 3*(x**2) # a=0, b=1,Er<0.3
    g = lambda x: math.e**-x - math.log(x,math.e) # a=1, b=1.5, Er<0.01
    h = lambda x: math.atan(x) + x -1 # a=0, b=1, Er<0.01


    biseccion(h,0,1,0.01,10)
    pass
