# config/settings.py
import os

# Dimensiones
ANCHO_VENTANA = 1200
ALTO_VENTANA = 800

# Colores
COLOR_FONDO = "#f0f0f0"
COLOR_BARRA_SUPERIOR = "#2c3e50"
COLOR_TEXTO_BLANCO = "#ffffff"
COLOR_VIA = "#95a5a6"
COLOR_ESTACION = "#34495e"
COLOR_TREN_IDA = "#e74c3c"    # Rojo para ir al Sur
COLOR_TREN_VUELTA = "#27ae60" # Verde para ir al Norte

# Rutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
