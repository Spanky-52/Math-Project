
import math
import itertools
import time


def validar_datos(n, k):

    if n < 0 or k < 0 or k > n:
        raise ValueError(
            "Los valores deben cumplir: 0 <= k <= n."
        )


# METODO 1: FORMULA MATEMATICA
def combinaciones_formula(n, k):

    validar_datos(n, k)

    resultado = (
        math.factorial(n) //
        (
            math.factorial(k) *
            math.factorial(n - k)
        )
    )

    return resultado


# METODO 2: GENERACION DE COMBINACIONES
def combinaciones_programacion(n, k):

    validar_datos(n, k)

    estudiantes = list(range(1, n + 1))

    equipos = itertools.combinations(estudiantes, k)

    cantidad = 0
    ejemplos = []

    for equipo in equipos:

        cantidad += 1

        if len(ejemplos) < 20:
            ejemplos.append(equipo)

    return cantidad, ejemplos


# COMPARACION DE LOS DOS METODOS
def comparar_combinaciones(n, k):

    # METODO MATEMATICO
    inicio = time.perf_counter()

    resultado_formula = combinaciones_formula(n, k)

    tiempo_formula = time.perf_counter() - inicio

    # METODO DE GENERACION
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


# COMPARACION PARA DIFERENTES VALORES
def comparar_diferentes_valores(k):

    valores_n = [5, 8, 10, 12, 15]

    resultados = {}

    for n in valores_n:

        if k <= n:

            datos = comparar_combinaciones(n, k)

            resultados[n] = datos

    return resultados
