"""Clase Persona y función para crear usuarios en la biblioteca."""
from datetime import date


class Persona:
    def __init__(self, id, nombre, libros=None):
        self.id = id
        self.nombre = nombre
        self.libros = libros if libros is not None else []

    def __str__(self):
        prestados = len(self.libros_prestados())
        return f"{self.id}: {self.nombre} - tiene {prestados} libro(s) prestado(s)"

    def libros_prestados(self):
        return [libro for libro in self.libros if libro["estado"] == "prestado"]

    def agregar_libro(self, libro, fecha=None):
        self.libros.append({
            "nombre": libro,
            "fecha": fecha or date.today().strftime("%d/%m/%Y"),
            "estado": "prestado",
        })

    def devolver_libro(self, libro) -> bool:
        for prestamo in self.libros_prestados():
            if prestamo["nombre"].lower() == libro.lower():
                prestamo["estado"] = "devuelto"
                return True
        return False

    def visualizar_libros(self):
        if not self.libros:
            print("   (no tiene libros registrados)")
        for i, libro in enumerate(self.libros, start=1):
            print(f"   {i}. {libro['nombre']}  |  {libro['fecha']}  |  {libro['estado']}")

    # Para guardar y cargar desde el archivo JSON
    def a_dict(self):
        return {"id": self.id, "nombre": self.nombre, "libros": self.libros}

    @classmethod
    def desde_dict(cls, datos):
        return cls(datos["id"], datos["nombre"], datos.get("libros", []))


def agregar_usuario(biblioteca: dict) -> Persona | None:
    id = input("Número de identificación: ").strip()
    if not id:
        print("La identificación no puede estar vacía.")
        return None
    if id in biblioteca:
        print(f"Ya existe un usuario con la identificación {id}.")
        return None

    nombre = input("¿Cuál es tu nombre?: ").strip() or "Sin nombre"
    persona = Persona(id, nombre)

    libro = input("¿Qué libro vas a prestar? (Enter para ninguno): ").strip()
    if libro:
        fecha = input("¿Qué día lo prestaste? (Enter = hoy): ").strip()
        persona.agregar_libro(libro, fecha or None)

    biblioteca[id] = persona
    print(f"Usuario creado: {persona}")
    return persona
