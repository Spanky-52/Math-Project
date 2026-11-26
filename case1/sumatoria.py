import time
import sys

# Ampliamos el limite de recursion por si probamos con n mayores a 1000
sys.setrecursionlimit(5000)

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
    # Formula de Gauss
    return (n * (n + 1)) // 2

def ejecutar_caso1():
    print("\n--- CASO 1: SUMATORIA DE UNA SECUENCIA ---")
    n = int(input("Ingresa el valor de n: "))

    if n < 0:
        print("El numero debe ser positivo.")
        return

    # 1. Metodo recursivo
    try:
        inicio = time.perf_counter()
        res_rec = suma_recursiva(n)
        t_rec = (time.perf_counter() - inicio) * 1000
        print(f"Recursiva -> Resultado: {res_rec} | Tiempo: {t_rec:.5f} ms")
    except RecursionError:
        print("Recursiva -> Error: se supero el limite de recursion en memoria.")

    # 2. Metodo iterativo
    inicio = time.perf_counter()
    res_ite = suma_iterativa(n)
    t_ite = (time.perf_counter() - inicio) * 1000
    print(f"Iterativa -> Resultado: {res_ite} | Tiempo: {t_ite:.5f} ms")

    # 3. Metodo constante
    inicio = time.perf_counter()
    res_con = suma_constante(n)
    t_con = (time.perf_counter() - inicio) * 1000
    print(f"Constante -> Resultado: {res_con} | Tiempo: {t_con:.5f} ms")