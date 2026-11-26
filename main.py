from caso1_sumatoria import ejecutar_caso_1
from caso2_combinaciones import ejecutar_caso_2


def mostrar_integrantes():
    """Muestra la lista de integrantes del equipo (Opción 3 del menú)."""
    print("\n" + "=" * 50)
    print("   INTEGRANTES DEL EQUIPO - MATEMÁTICA DISCRETA 1")
    print("=" * 50)
    integrantes = [
        "1. Ventura Apaza Henry Joseph",
        "2. Aguilar Calizaya Anderson Michael",
        "3. Zeballos de la Cruz Yadira Melani"
    ]
    for persona in integrantes:
        print(persona)
    print("=" * 50)


def menu_principal():
    """Interfaz de usuario básica en consola con las 4 opciones requeridas."""
    while True:
        print("\n" + "*" * 50)
        print("   MENÚ PRINCIPAL - TRABAJO PRÁCTICO GRUPAL")
        print("   Asignatura: Matemática Discreta 1")
        print("*" * 50)
        print("1. Caso de Estudio I: Sumatoria de una Secuencia")
        print("2. Caso de Estudio II: Combinaciones de Equipos")
        print("3. Mostrar los integrantes del equipo")
        print("4. Finalizar la aplicación")
        print("*" * 50)

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            ejecutar_caso_1()
        elif opcion == "2":
            ejecutar_caso_2()
        elif opcion == "3":
            mostrar_integrantes()
        elif opcion == "4":
            print("\nFinalizando la aplicación... ¡Hasta pronto!")
            break
        else:
            print("\n⚠️ Opción no válida. Por favor, ingrese un número del 1 al 4.")


if __name__ == "__main__":
    menu_principal()