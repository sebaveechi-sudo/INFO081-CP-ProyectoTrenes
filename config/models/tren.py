# models/tren.py

class Tren:
    def __init__(self, id_tren, modelo, capacidad_maxima, velocidad):
        self.id_tren = id_tren
        self.modelo = modelo
        self.capacidad_maxima = capacidad_maxima
        self.velocidad = velocidad
        self.vagones = []
        self.estado = "EN_ESPERA"

    def __str__(self):
        return f"Tren {self.id_tren} ({self.modelo})"
