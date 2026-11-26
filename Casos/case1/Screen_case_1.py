
import tkinter as tk
from tkinter import messagebox

from Casos.case1.Algoritmos import (
    comparar_algoritmos,
    ejecutar_pruebas
)


def mostrar_caso1(contenedor, volver):

    for widget in contenedor.winfo_children():
        widget.destroy()

    contenedor.configure(bg="#ecf0f1")

    tk.Label(
        contenedor,
        text="CASO 1 - CALCULO DE SUMATORIA",
        font=("Arial", 19, "bold"),
        bg="#ecf0f1",
        fg="#2c3e50"
    ).pack(pady=15)

    tk.Label(
        contenedor,
        text="Ingrese la cantidad de numeros (n):",
        font=("Arial", 11),
        bg="#ecf0f1"
    ).pack(pady=5)

    entrada_n = tk.Entry(
        contenedor,
        font=("Arial", 12),
        justify="center",
        width=20
    )

    entrada_n.pack(pady=5)

    resultados = tk.Label(
        contenedor,
        text="Los resultados apareceran aqui.",
        font=("Consolas", 10),
        bg="white",
        fg="#2c3e50",
        justify="left",
        anchor="nw",
        width=95,
        height=16,
        wraplength=760,
        padx=15,
        pady=10,
        relief="solid",
        bd=1
    )

    resultados.pack(pady=12)

    def ejecutar():

        try:

            n = int(entrada_n.get())

            if n < 0:
                raise ValueError

            datos = comparar_algoritmos(n)

            texto = (
                "RESULTADOS DE LA SUMATORIA\n"
                "----------------------------------------\n\n"
                f"Valor de n: {n}\n\n"
            )

            for metodo in ["recursiva", "iterativa", "constante"]:

                info = datos[metodo]

                texto += f"METODO {metodo.upper()}\n"

                if info["tiempo"] is not None:

                    texto += (
                        f"Resultado: {info['resultado']}\n"
                        f"Tiempo: {info['tiempo']:.8f} ms\n"
                    )

                else:

                    texto += (
                        f"Estado: {info['estado']}\n"
                    )

                texto += "\n"

            texto += (
                "----------------------------------------\n"
                "COMPLEJIDAD ALGORITMICA\n\n"
                "Recursiva: O(n)\n"
                "Iterativa: O(n)\n"
                "Constante: O(1)\n"
            )

            resultados.config(text=texto)

        except ValueError:

            messagebox.showerror(
                "Error",
                "Ingrese un numero entero mayor o igual a cero."
            )

    def pruebas():

        datos = ejecutar_pruebas()

        texto = (
            "COMPARACION PARA DIFERENTES VALORES DE N\n"
            "------------------------------------------------\n\n"
        )

        for n, metodos in datos.items():

            texto += f"VALOR DE N: {n}\n"

            for metodo, info in metodos.items():

                if info["tiempo"] is not None:

                    texto += (
                        f"{metodo.capitalize()}: "
                        f"{info['tiempo']:.8f} ms\n"
                    )

                else:

                    texto += (
                        f"{metodo.capitalize()}: "
                        "No disponible\n"
                    )

            texto += "\n"

        resultados.config(text=texto)

    tk.Button(
        contenedor,
        text="Ejecutar Algoritmos",
        font=("Arial", 10, "bold"),
        bg="#3498db",
        fg="white",
        width=25,
        command=ejecutar
    ).pack(pady=4)

    tk.Button(
        contenedor,
        text="Comparar Diferentes Valores de N",
        font=("Arial", 10, "bold"),
        bg="#27ae60",
        fg="white",
        width=30,
        command=pruebas
    ).pack(pady=4)

    tk.Button(
        contenedor,
        text="Volver al Menu Principal",
        font=("Arial", 10),
        command=volver
    ).pack(pady=8)
