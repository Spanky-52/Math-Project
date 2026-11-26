
import tkinter as tk
from tkinter import messagebox

from Casos.case2.Algoritmos import (
    comparar_combinaciones,
    comparar_diferentes_valores
)


def mostrar_caso2(contenedor, volver):

    for widget in contenedor.winfo_children():
        widget.destroy()

    contenedor.configure(bg="#ecf0f1")

    tk.Label(
        contenedor,
        text="CASO 2 - COMBINACIONES DE EQUIPOS",
        font=("Arial", 19, "bold"),
        bg="#ecf0f1",
        fg="#2c3e50"
    ).pack(pady=12)

    # ENTRADA N
    tk.Label(
        contenedor,
        text="Cantidad de estudiantes (n):",
        font=("Arial", 11),
        bg="#ecf0f1"
    ).pack(pady=4)

    entrada_n = tk.Entry(
        contenedor,
        font=("Arial", 12),
        justify="center",
        width=20
    )

    entrada_n.pack(pady=4)

    # ENTRADA K
    tk.Label(
        contenedor,
        text="Integrantes por equipo (k):",
        font=("Arial", 11),
        bg="#ecf0f1"
    ).pack(pady=4)

    entrada_k = tk.Entry(
        contenedor,
        font=("Arial", 12),
        justify="center",
        width=20
    )

    entrada_k.pack(pady=4)

    # RESULTADOS NO EDITABLES
    resultados = tk.Label(
        contenedor,
        text="Los resultados apareceran aqui.",
        font=("Consolas", 9),
        bg="white",
        fg="#2c3e50",
        justify="left",
        anchor="nw",
        width=95,
        height=15,
        wraplength=760,
        padx=12,
        pady=10,
        relief="solid",
        bd=1
    )

    resultados.pack(pady=10)

    # EJECUTAR COMBINACIONES
    def ejecutar():

        try:

            n = int(entrada_n.get())
            k = int(entrada_k.get())

            if n < 0 or k < 0 or k > n:
                raise ValueError

            if n > 20:

                messagebox.showwarning(
                    "Limite de participantes",
                    "Ingrese un maximo de 20 participantes "
                    "para controlar el tiempo de generacion."
                )

                return

            datos = comparar_combinaciones(n, k)

            texto = (
                "RESULTADOS DE LAS COMBINACIONES\n"
                "----------------------------------------\n\n"
                f"Participantes: {n}\n"
                f"Integrantes por equipo: {k}\n\n"
                "COMPARACION DE METODOS\n\n"
                f"Cantidad mediante formula: "
                f"{datos['formula']}\n"

                f"Cantidad mediante generacion: "
                f"{datos['generacion']}\n\n"

                f"Tiempo formula: "
                f"{datos['tiempo_formula']:.10f} segundos\n"

                f"Tiempo generacion: "
                f"{datos['tiempo_generacion']:.10f} segundos\n\n"

                "EQUIPOS GENERADOS (MAXIMO 20)\n"
                "----------------------------------------\n"
            )

            for indice, equipo in enumerate(
                datos["equipos"],
                start=1
            ):

                texto += f"Equipo {indice}: {equipo}\n"

            texto += "\nVERIFICACION DE RESULTADOS\n"

            if datos["formula"] == datos["generacion"]:

                texto += (
                    "Ambos metodos producen el mismo resultado."
                )

            else:

                texto += (
                    "Existe una diferencia entre los resultados."
                )

            resultados.config(text=texto)

        except ValueError:

            messagebox.showerror(
                "Error",
                "Ingrese valores enteros validos.\n"
                "Debe cumplirse: 0 <= k <= n."
            )

    # COMPARAR DIFERENTES N
    def comparar():

        try:

            k = int(entrada_k.get())

            if k < 0 or k > 20:
                raise ValueError

            datos = comparar_diferentes_valores(k)

            texto = (
                "COMPARACION PARA DIFERENTES VALORES DE N\n"
                "----------------------------------------\n\n"
                f"Integrantes por equipo: {k}\n\n"
            )

            for n, info in datos.items():

                texto += f"PARTICIPANTES: {n}\n"

                texto += (
                    f"Formula: {info['formula']}\n"
                    f"Generacion: {info['generacion']}\n"
                    f"Tiempo formula: "
                    f"{info['tiempo_formula']:.10f} s\n"
                    f"Tiempo generacion: "
                    f"{info['tiempo_generacion']:.10f} s\n\n"
                )

            resultados.config(text=texto)

        except ValueError:

            messagebox.showerror(
                "Error",
                "Ingrese un valor valido de k."
            )

    tk.Button(
        contenedor,
        text="Generar Combinaciones",
        font=("Arial", 10, "bold"),
        bg="#3498db",
        fg="white",
        width=28,
        command=ejecutar
    ).pack(pady=4)

    tk.Button(
        contenedor,
        text="Comparar Diferentes Valores de N",
        font=("Arial", 10, "bold"),
        bg="#27ae60",
        fg="white",
        width=32,
        command=comparar
    ).pack(pady=4)

    tk.Button(
        contenedor,
        text="Volver al Menu Principal",
        font=("Arial", 10),
        command=volver
    ).pack(pady=5)
