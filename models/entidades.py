from datetime import timedelta
import random

class Vagon:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = []

    def get_ocupacion(self):
        return len(self.pasajeros)

    def to_dict(self):
        return {"capacidad": self.capacidad, "ocupacion": len(self.pasajeros)}

class Pasajero:
    def __init__(self, id_p, origen_id, destino_id, hora_creacion):
        self.id = id_p
        self.origen_id = origen_id
        self.destino_id = destino_id
        self.fecha_creacion = hora_creacion
        
        rng = random.Random(self.id)
        minutos_estadia = rng.randint(30, 4320)
        self.fecha_deseada_regreso = self.fecha_creacion + timedelta(minutes=minutos_estadia)

    def to_dict(self):
        return {
            "id": self.id,
            "origen": self.origen_id,
            "destino": self.destino_id,
            "creacion": self.fecha_creacion.strftime("%Y-%m-%d %H:%M:%S"),
            "regreso": self.fecha_deseada_regreso.strftime("%Y-%m-%d %H:%M:%S")
        }

class Estacion:
    def __init__(self, id_est, nombre, km_ubicacion, poblacion, vias_por_sentido=2):
        self.id = id_est
        self.nombre = nombre
        self.km = km_ubicacion
        self.poblacion = poblacion
        self.cola_pasajeros = []
        
        self.capacidad_vias = vias_por_sentido
        self.vias = {1: [], -1: []}
        self.via_rotacion = None 

    def hay_via_disponible(self, direccion):
        return len(self.vias[direccion]) < self.capacidad_vias

    def ocupar_via(self, tren, direccion):
        if self.hay_via_disponible(direccion):
            self.vias[direccion].append(tren)
            return True
        return False

    def liberar_via(self, tren, direccion):
        if tren in self.vias[direccion]:
            self.vias[direccion].remove(tren)

    def ocupar_rotacion(self, tren):
        if self.via_rotacion is None:
            self.via_rotacion = tren
            return True
        return False

    def liberar_rotacion(self):
        self.via_rotacion = None

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "km": self.km,
            "poblacion": self.poblacion,
            "pasajeros_esperando": len(self.cola_pasajeros)
        }

class Tren:
    def __init__(self, id_tren, modelo, velocidad_max, km_actual=0):
        self.id = id_tren
        self.nombre = modelo
        self.velocidad_max = velocidad_max
        self.km_actual = km_actual
        self.direccion = 1 
        self.estado = "EN_ESTACION" 
        self.tiempo_proceso = 0 
        self.vagones = []
        
        if "BMU" in modelo:
            for _ in range(4): self.vagones.append(Vagon(60))
        else:
            num = random.randint(2, 5)
            for _ in range(num): self.vagones.append(Vagon(70))

    def get_capacidad_total(self):
        return sum(v.capacidad for v in self.vagones)

    def get_ocupacion_total(self):
        return sum(v.get_ocupacion() for v in self.vagones)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "km_actual": self.km_actual,
            "direccion": self.direccion,
            "estado": self.estado,
            "vagones": [v.to_dict() for v in self.vagones]
        }
