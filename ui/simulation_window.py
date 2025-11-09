# ui/simulation_window.py
import tkinter as tk
from config import settings

class SimulationWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        label = tk.Label(self, text="Pantalla Principal de Simulación", font=("Arial", 18))
        label.pack(pady=20)

        btn_volver = tk.Button(self, text="Volver al Menú", command=lambda: controller.show_frame("MenuWindow"))
        btn_volver.pack(pady=10)

        # Aquí irían los indicadores (RF07) y el mapa en el futuro
