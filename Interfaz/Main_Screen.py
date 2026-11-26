import tkinter as tk
from tkinter import messagebox

#from Casos.case1
from Casos.case2.Screen_case_2 import mostrar_caso2


class MainScreen:

    def __init__(self, root):
        self.root = root
        self.root.title("Proyecto - Análisis de Algoritmos")
        self.root.geometry("850x600")
        self.root.resizable(False, False)

        self.contenedor = tk.Frame(root, padx=30, pady=25)
        self.contenedor.pack(fill="both", expand=True)

        self.mostrar_menu()

    def limpiar(self):
        for widget in self.contenedor.winfo_children():
            widget.destroy()

    def mostrar_menu(self):
        self.limpiar()

        tk.Label(
            self.contenedor,
            text="ANÁLISIS DE ALGORITMOS",
            font=("Arial", 23, "bold")
        ).pack(pady=25)

        tk.Label(
            self.contenedor,
            text="Seleccione una opción del menú",
            font=("Arial", 12)
        ).pack(pady=10)

        tk.Button(
            self.contenedor,
            text="Caso 1 - Cálculo de Sumatoria",
            font=("Arial", 12),
            width=35,
            height=2,
            command=lambda: mostrar_caso1(
                self.contenedor, self.mostrar_menu
            )
        ).pack(pady=12)

        tk.Button(
            self.contenedor,
            text="Caso 2 - Combinaciones de Equipos",
            font=("Arial", 12),
            width=35,
            height=2,
            command=lambda: mostrar_caso2(
                self.contenedor, self.mostrar_menu
            )
        ).pack(pady=12)

        tk.Button(
            self.contenedor,
            text="Mostrar Integrantes del Equipo",
            font=("Arial", 12),
            width=35,
            height=2,
            command=self.mostrar_integrantes
        ).pack(pady=12)

        tk.Button(
            self.contenedor,
            text="Finalizar Aplicación",
            font=("Arial", 12),
            width=35,
            height=2,
            bg="#c0392b",
            fg="white",
            command=self.finalizar
        ).pack(pady=12)

    def mostrar_integrantes(self):
        messagebox.showinfo(
            "Integrantes",
            "Integrantes del equipo:\n\n"
            "1. Integrante 1\n"
            "2. Integrante 2\n"
            "3. Integrante 3"
        )

    def finalizar(self):
        if messagebox.askyesno(
            "Salir",
            "¿Desea finalizar la aplicación?"
        ):
            self.root.destroy()