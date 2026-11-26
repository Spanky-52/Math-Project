import tkinter as tk
from tkinter import messagebox

from Casos.case1.Screen_case_1 import mostrar_caso1
from Casos.case2.Screen_case_2 import mostrar_caso2


class MainScreen:

    def __init__(self, root):
        self.root = root

        self.root.title("Proyecto - Análisis de Algoritmos")
        self.root.geometry("850x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#ecf0f1")

        self.contenedor = tk.Frame(
            self.root,
            bg="#ecf0f1",
            padx=30,
            pady=25
        )

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
            font=("Arial", 24, "bold"),
            bg="#ecf0f1",
            fg="#2c3e50"
        ).pack(pady=30)

        tk.Label(
            self.contenedor,
            text="Seleccione una opción del menú principal",
            font=("Arial", 12),
            bg="#ecf0f1"
        ).pack(pady=10)

        tk.Button(
            self.contenedor,
            text="Caso 1 - Cálculo de Sumatoria",
            font=("Arial", 12, "bold"),
            width=38,
            height=2,
            bg="#3498db",
            fg="white",
            command=lambda: mostrar_caso1(
                self.contenedor,
                self.mostrar_menu
            )
        ).pack(pady=12)

        tk.Button(
            self.contenedor,
            text="Caso 2 - Combinaciones de Equipos",
            font=("Arial", 12, "bold"),
            width=38,
            height=2,
            bg="#2980b9",
            fg="white",
            command=lambda: mostrar_caso2(
                self.contenedor,
                self.mostrar_menu
            )
        ).pack(pady=12)

        tk.Button(
            self.contenedor,
            text="Mostrar Integrantes del Equipo",
            font=("Arial", 12, "bold"),
            width=38,
            height=2,
            bg="#27ae60",
            fg="white",
            command=self.mostrar_integrantes
        ).pack(pady=12)

        tk.Button(
            self.contenedor,
            text="Finalizar Aplicación",
            font=("Arial", 12, "bold"),
            width=38,
            height=2,
            bg="#c0392b",
            fg="white",
            command=self.finalizar
        ).pack(pady=12)

    def mostrar_integrantes(self):

        self.limpiar()

        # Lista de integrantes
        integrantes = [
            "Aguilar Calizaya Anderson Michael",
            "Ventura Apaza Henry Jhosep",
            "Zeballos de la Cruz Yadira Melani"
        ]

        tk.Label(
            self.contenedor,
            text="INTEGRANTES DEL EQUIPO",
            font=("Arial", 22, "bold"),
            bg="#ecf0f1",
            fg="#2c3e50"
        ).pack(pady=30)

        # Recorrer la lista de integrantes
        for integrante in integrantes:
            tk.Label(
                self.contenedor,
                text=integrante,
                font=("Arial", 15),
                bg="white",
                fg="#2c3e50",
                width=40,
                pady=12,
                relief="solid",
                bd=1
            ).pack(pady=8)

        # Botón para regresar
        tk.Button(
            self.contenedor,
            text="Volver al Menu Principal",
            font=("Arial", 11, "bold"),
            bg="#3498db",
            fg="white",
            width=30,
            command=self.mostrar_menu
        ).pack(pady=30)

    def finalizar(self):

        respuesta = messagebox.askyesno(
            "Finalizar Aplicación",
            "¿Está seguro de que desea salir?"
        )

        if respuesta:
            self.root.destroy()
