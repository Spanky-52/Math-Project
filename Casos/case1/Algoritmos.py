import time


def suma_recursiva(n):

    if n <= 1:
        return n

    return n + suma_recursiva(n - 1)


def suma_iterativa(n):

    suma = 0

    for i in range(1, n + 1):
        suma += i

    return suma


def suma_constante(n):

    return (n * (n + 1)) // 2


def comparar_algoritmos(n):

    resultados = {}

    # METODO RECURSIVO
    try:
        inicio = time.perf_counter()

        resultado = suma_recursiva(n)

        tiempo = (time.perf_counter() - inicio) * 1000

        resultados["recursiva"] = {
            "resultado": resultado,
            "tiempo": tiempo,
            "estado": "Correcto"
        }

    except RecursionError:

        resultados["recursiva"] = {
            "resultado": None,
            "tiempo": None,
            "estado": "Limite de recursion superado"
        }

    # METODO ITERATIVO
    inicio = time.perf_counter()

    resultado = suma_iterativa(n)

    tiempo = (time.perf_counter() - inicio) * 1000

    resultados["iterativa"] = {
        "resultado": resultado,
        "tiempo": tiempo,
        "estado": "Correcto"
    }

    # METODO CONSTANTE
    inicio = time.perf_counter()

    resultado = suma_constante(n)

    tiempo = (time.perf_counter() - inicio) * 1000

    resultados["constante"] = {
        "resultado": resultado,
        "tiempo": tiempo,
        "estado": "Correcto"
    }

    return resultados


def ejecutar_pruebas():

    valores = [10, 100, 500, 900]

    comparaciones = {}

    for n in valores:

        comparaciones[n] = comparar_algoritmos(n)

    return comparaciones
