#!/usr/bin/env python3
"""
Proyecto en Python sobre el Algoritmo de Bisección.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

import math


def biseccion(f, a, b, ER, N):

        i = 0
        intInf = a
        intMay = b
        pmActual = 0

        getRelativeError = lambda: abs((intInf - intMay)/intMay)

        getMiddlePoint = lambda: (intInf + intMay)/2

        while i <= N:
            i += 1
            pmActual = getMiddlePoint()
            error = getRelativeError()

            print("Iteración:", i, "Punto Medio:", pmActual, "Error:", error)

            if error < ER:
                print("Error aproximado de", ER, ":", error)
                print("Comprobación de f(", pmActual, ")", ":", f(pmActual))
                return pmActual

            if (f(pmActual) * f(intMay)) > 0 and (f(pmActual) * f(intInf)) > 0 :
                print("No se pueden realizar mas operaciones.")
                return pmActual

            if (f(pmActual) * f(intMay)) < 0:
                intInf = pmActual

            if (f(pmActual) * f(intInf)) < 0:
                intMay = pmActual

        else:
            print("Se alcanzó el limite de iteraciones.")
            return pmActual


if __name__ == "__main__":
    f = lambda x: math.exp(x) - 3*(x**2)
    biseccion(f, 0, 1, 0.03, 10)
    pass
