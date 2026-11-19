"""Buscar y ver un usuario de la biblioteca."""


def buscar_usuario(biblioteca: dict):
    id = input("Identificación del usuario: ").strip()
    persona = biblioteca.get(id)
    if persona is None:
        print(f"No existe un usuario con la identificación {id}.")
    return persona


def visualizar_usuario(biblioteca: dict) -> None:
    persona = buscar_usuario(biblioteca)
    if persona:
        print(persona)
        persona.visualizar_libros()
