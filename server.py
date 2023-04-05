import tkinter as tk
from tkinter import ttk

class GUI:
    def __init__(self, root):
        self.master = root
        self.master.title("Weather App")
        
        pass

if __name__ == "__main__":
    root = tk.Tk()
    user_interface = GUI(root)
    root.mainloop()