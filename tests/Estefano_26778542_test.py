#!/usr/bin/env python3

import sys
import math
sys.path.append("../")

from Estefano_26778542 import biseccion

# CASOS DE PRUEBA:

f = lambda x: math.exp(-x) - math.log(x)
g = lambda x: x - math.cos(x)
h = lambda x: x**2 - 5*x - math.exp(x)

casos_prueba = ((f, 1, 2, 0.02, 20),
               (g, 0, 1, 0.02, 20),
                (h, -1, 1, 0.02, 20))

# SOLUCIONES:

# CASO 0:
# Raíz: 1.296875
# Comprobación: f(1.296875) = 0.013427262559215503

# CASO 1:
# Raíz: 0.7421875
# Comprobación: f(0.7421875) = 0.005195711743759213

# CASO 2:
# Raíz: -0.166015625
# Comprobación: f(-0.166015625) = 0.010606313548751523

for i, caso in enumerate(casos_prueba):
    print("Caso:", i)
    try:
        raiz = biseccion(*caso)
    except:
        print("FALLÓ.")
        continue
    print("Raíz:", raiz)
    print("Comprobación: f({}) = {}\n".format(raiz, caso[0](raiz)))

# RESULTADOS:

# CASO 0: OK.
# CASO 1: OK.
# CASO 2: OK.
# OBSERVACIONES: Presenta alta similitud con el código en el repositorio.
# NOTA: 8.