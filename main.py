from case1.sumatoria import ejecutar_caso1
from case2.combinacionesss import ejecutar_caso2

def mostrar_integrantes():
    print("\nINTEGRANTES DEL EQUIPO Moscu")
    print("1. Aguilar Calizaya Anderson Michael")
    print("2. Ventura Apaza Henry Joseph")
    print("3. Zeballos de la Cruz Yadira Melani")

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Caso 1: Sumatoria de una secuencia")
        print("2. Caso 2: Combinaciones de equipos")
        print("3. Mostrar integrantes")
        print("4. Salir")

        opcion = input("Elige una opcion: ")

        if opcion == "1":
            ejecutar_caso1()
        elif opcion == "2":
            ejecutar_caso2()
        elif opcion == "3":
            mostrar_integrantes()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion incorrecta, intenta de nuevo.")

if __name__ == "__main__":
    menu()