import math
import itertools
import time


def combinaciones_formula(n, k):

    if n < 0 or k < 0 or k > n:
        raise ValueError("Valores de n y k no válidos.")

    resultado = (
        math.factorial(n) //
        (
            math.factorial(k) *
            math.factorial(n - k)
        )
    )

    return resultado


def combinaciones_programacion(n, k):

    if n < 0 or k < 0 or k > n:
        raise ValueError("Valores de n y k no válidos.")

    estudiantes = list(range(1, n + 1))

    equipos = itertools.combinations(estudiantes, k)

    cantidad = 0
    ejemplos = []

    for equipo in equipos:

        cantidad += 1

        if len(ejemplos) < 20:
            ejemplos.append(equipo)

    return cantidad, ejemplos


# COMPARACION DE METODOS
def comparar_combinaciones(n, k):

    inicio = time.perf_counter()

    resultado_formula = combinaciones_formula(n, k)

    tiempo_formula = time.perf_counter() - inicio

    inicio = time.perf_counter()

    resultado_programacion, equipos = (
        combinaciones_programacion(n, k)
    )

    tiempo_programacion = time.perf_counter() - inicio

    return {
        "formula": resultado_formula,
        "generacion": resultado_programacion,
        "equipos": equipos,
        "tiempo_formula": tiempo_formula,
        "tiempo_generacion": tiempo_programacion
    }