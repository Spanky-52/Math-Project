import tkinter as tk
from tkinter import messagebox

from casos.caso2_combinaciones.algoritmos import (
    comparar_combinaciones
)


def mostrar_caso2(contenedor, volver):

    for widget in contenedor.winfo_children():
        widget.destroy()

    tk.Label(
        contenedor,
        text="CASO 2 - COMBINACIONES DE EQUIPOS",
        font=("Arial", 19, "bold")
    ).pack(pady=15)

    tk.Label(
        contenedor,
        text="Cantidad de estudiantes (n):",
        font=("Arial", 11)
    ).pack(pady=5)

    entrada_n = tk.Entry(
        contenedor,
        font=("Arial", 12),
        justify="center"
    )
    entrada_n.pack(pady=5)

    tk.Label(
        contenedor,
        text="Cantidad de integrantes por equipo (k):",
        font=("Arial", 11)
    ).pack(pady=5)

    entrada_k = tk.Entry(
        contenedor,
        font=("Arial", 12),
        justify="center"
    )
    entrada_k.pack(pady=5)

    resultados = tk.Text(
        contenedor,
        height=13,
        width=85,
        font=("Consolas", 10)
    )
    resultados.pack(pady=12)

    def ejecutar():

        try:
            n = int(entrada_n.get())
            k = int(entrada_k.get())

            if n < 0 or k < 0 or k > n:
                raise ValueError

            if n > 20:
                messagebox.showwarning(
                    "Límite de participantes",
                    "Ingrese un máximo de 20 participantes "
                    "para limitar el tiempo de generación."
                )
                return

            datos = comparar_combinaciones(n, k)

            resultados.delete("1.0", tk.END)

            resultados.insert(
                tk.END,
                "RESULTADOS DE LAS COMBINACIONES\n"
            )

            resultados.insert(
                tk.END,
                "-" * 65 + "\n"
            )

            resultados.insert(
                tk.END,
                f"Participantes: {n}\n"
            )

            resultados.insert(
                tk.END,
                f"Integrantes por equipo: {k}\n\n"
            )

            resultados.insert(
                tk.END,
                f"Cantidad mediante fórmula: "
                f"{datos['formula']}\n"
            )

            resultados.insert(
                tk.END,
                f"Cantidad mediante generación: "
                f"{datos['generacion']}\n\n"
            )

            resultados.insert(
                tk.END,
                f"Tiempo fórmula: "
                f"{datos['tiempo_formula']:.10f} segundos\n"
            )

            resultados.insert(
                tk.END,
                f"Tiempo generación: "
                f"{datos['tiempo_generacion']:.10f} segundos\n\n"
            )

            resultados.insert(
                tk.END,
                "EQUIPOS GENERADOS (MÁXIMO 20)\n"
            )

            resultados.insert(
                tk.END,
                "-" * 65 + "\n"
            )

            for indice, equipo in enumerate(
                datos["equipos"], start=1
            ):

                resultados.insert(
                    tk.END,
                    f"Equipo {indice}: {equipo}\n"
                )

            resultados.insert(
                tk.END,
                "\nVERIFICACIÓN:\n"
            )

            if datos["formula"] == datos["generacion"]:

                resultados.insert(
                    tk.END,
                    "Ambos métodos producen el mismo resultado."
                )

            else:

                resultados.insert(
                    tk.END,
                    "Existe una diferencia entre los resultados."
                )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Ingrese valores enteros válidos. "
                "Debe cumplirse: 0 <= k <= n."
            )

    tk.Button(
        contenedor,
        text="Generar combinaciones",
        font=("Arial", 11, "bold"),
        command=ejecutar
    ).pack(pady=5)

    tk.Button(
        contenedor,
        text="Volver al menú principal",
        font=("Arial", 10),
        command=volver
    ).pack(pady=5)