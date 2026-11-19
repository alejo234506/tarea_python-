"""Eliminar un usuario de la biblioteca."""


def eliminar_usuario(biblioteca: dict) -> bool:
    id = input("Identificación del usuario a eliminar: ").strip()
    persona = biblioteca.get(id)
    if persona is None:
        print(f"No existe un usuario con la identificación {id}.")
        return False

    if persona.libros_prestados():
        print(f"Ojo: {persona.nombre} todavía tiene {len(persona.libros_prestados())} libro(s) sin devolver.")

    confirmar = input(f"¿Seguro que quieres eliminar a {persona.nombre}? (s/n): ").strip().lower()
    if confirmar == "s":
        del biblioteca[id]
        print("Usuario eliminado.")
        return True
    print("No se eliminó nada.")
    return False
