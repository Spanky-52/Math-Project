import tkinter as tk
from interfaz.main_screen import MainScreen


def main():
    root = tk.Tk()
    app = MainScreen(root)
    root.mainloop()


if __name__ == "__main__":
    main()