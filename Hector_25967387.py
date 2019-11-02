#!/usr/bin/env python3
import math
def signo(f,a,b):
    return (f(a)  *  f(b))

def relerr(act,ant):
    return math.fabs((act-ant)/act)

def biseccion (f, a, b, ER, N):
    """
    Implementa el Algoritmo de Biseccion y retorna la aproximación de la raiz.
    Parámetros:
    f: función de variable real f(x).
    a: límite inferior del intervalo.
    b: límite superior del intervalo.
    ER: cota mínima del error relativo.
    N: número máximo de iteraciones.
    """
    rel = 100 #Aproximacion de error relativo
    it = 1 #Contador de iteraciones.
    mat = 0 #Punto medio actual
    man = 0 # Punto medio anterior
    if (signo(f, a, b)) < 0:
        for it in range(rel):
            if(rel>ER):
                man = mat
                mat = (a+b)/2
                if (signo(f, a, mat)) < 0:
                    b = mat
                else:
                    a = mat
                rel = relerr(mat,man)
                it=it+1
                print("Iteración:", it, "Punto Medio:", mat, "Error:", rel)
        return mat
    else:
        print ("Esta funcion, o los puntos asignados no cumplen el teorema de valor intermedio-")

if __name__ == "__main__":
    # Pruebe aquí su función.
  f = lambda x: 8 - 2*x**2 -x**3

    biseccion(f, 1, 3, 0.03, 100)
