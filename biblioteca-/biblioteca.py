"""Biblioteca: programa principal con menú.

Lleva el registro de las personas y los libros que tienen prestados.
Los datos se guardan en biblioteca.json, así no se pierden al cerrar.

Ejecutar:  py biblioteca-/biblioteca.py
"""
import json
from pathlib import Path

from biblioteca_crear import Persona, agregar_usuario
from biblioteca_actualizar import actualizar_usuario
from biblioteca_visualizar import visualizar_usuario
from biblioteca_imprimir import imprimir_todos
from biblioteca_remover import eliminar_usuario

ARCHIVO = Path(__file__).with_name("biblioteca.json")


def cargar() -> dict:
    if not ARCHIVO.exists():
        return {}
    try:
        datos = json.loads(ARCHIVO.read_text(encoding="utf-8"))
        return {d["id"]: Persona.desde_dict(d) for d in datos}
    except (json.JSONDecodeError, KeyError):
        print("No se pudo leer biblioteca.json, se empieza con la biblioteca vacía.")
        return {}


def guardar(biblioteca: dict) -> None:
    datos = [persona.a_dict() for persona in biblioteca.values()]
    ARCHIVO.write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8")


def menu():
    biblioteca = cargar()
    opciones = {
        "1": actualizar_usuario,
        "2": visualizar_usuario,
        "3": imprimir_todos,
        "4": eliminar_usuario,
        "0": agregar_usuario,
    }

    while True:
        print("*" * 60)
        opcion = input("""Este menú es para adquirir un libro en una biblioteca
      [0] crear un usuario nuevo
      [1] actualizar el usuario (nombre, prestar o devolver libro)
      [2] visualizar un usuario
      [3] ver todos los usuarios
      [4] eliminar el usuario
      [5] cerrar
      - INGRESA EL NÚMERO: """).strip()

        if opcion == "5":
            print("¡Hasta luego!")
            break
        if opcion in opciones:
            opciones[opcion](biblioteca)
            guardar(biblioteca)
        else:
            print("Opción no válida, escribe un número del 0 al 5.")
        print("-" * 60)


if __name__ == "__main__":
    menu()
