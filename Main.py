import tkinter as tk
from Interfaz.Main_Screen import MainScreen


def main():
    root = tk.Tk()
    app = MainScreen(root)
    root.mainloop()


if __name__ == "__main__":
    main()