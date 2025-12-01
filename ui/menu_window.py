import tkinter as tk
from tkinter import messagebox 
from config import settings
import os

class MenuWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg=settings.COLOR_FONDO)
        label = tk.Label(self, text="Simulador de Tráfico Ferroviario EFE", 
                         font=("Arial", 24, "bold"), bg=settings.COLOR_FONDO, fg=settings.COLOR_TEXTO_MORADO)
        label.pack(pady=50)
        btn_nueva = tk.Button(self, text="Nueva Simulación", 
                              command=lambda: controller.show_frame("SimulationWindow"), 
                              width=25, height=2, font=("Arial", 12))
        btn_nueva.pack(pady=10)
        def realizar_carga():
            ruta = os.path.join(settings.DATA_DIR, "partida_guardada.json")
            if not os.path.exists(ruta):
                messagebox.showwarning("Aviso", "No se encontró ningún archivo de guardado.\n\nInicia una nueva simulación y guárdala primero.")
                return 
            controller.estado_simulacion.cargar_partida()
            controller.show_frame("SimulationWindow")
        btn_cargar = tk.Button(self, text="Cargar Simulación", 
                               command=realizar_carga,
                               width=25, height=2, font=("Arial", 12))
        btn_cargar.pack(pady=10)
        btn_salir = tk.Button(self, text="Salir", command=parent.quit, 
                              width=25, height=2, font=("Arial", 12), bg="#e74c3c", fg="white")
        btn_salir.pack(pady=10)
