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
    if f(a)*f(b) < 0:
        it=1
        P_Medioactual=0
        P_Medioprevio=0
        e=100;
        while (it<N)&(e>ER):
            P_Medioprevio=P_Medioactual
            P_Medioactual=(a+b)/2
            if f(P_Medioactual)*f(b)<0:
                a=P_Medioactual
            else:
                b=P_Medioactual
            if it>1:
                e=abs(P_Medioactual-P_Medioprevio/P_Medioactual)
            it=it+1
            print("Iteración:", it, "Punto Medio:", P_Medioactual, "Error:", e)  

        return P_Medioactual
    else:
        print ("El intervalo no es valido.")

if __name__ == "__main__":
    # Pruebe aquí su función.
    f=lambda x:(math.e)**x-3*(x**2)
    biseccion(f,0,1,0.03,100)
    pass
