"""Actualizar un usuario: cambiar el nombre, prestar un libro o devolverlo."""
from biblioteca_visualizar import buscar_usuario


def actualizar_usuario(biblioteca: dict) -> None:
    persona = buscar_usuario(biblioteca)
    if persona is None:
        return

    opcion = input("""¿Qué quieres hacer?
      [1] cambiar el nombre
      [2] prestar un libro
      [3] devolver un libro
      -> """).strip()

    if opcion == "1":
        nuevo = input(f"Nuevo nombre (actual: {persona.nombre}): ").strip()
        if nuevo:
            persona.nombre = nuevo
            print("Nombre actualizado.")
    elif opcion == "2":
        libro = input("Nombre del libro: ").strip()
        if libro:
            fecha = input("Fecha del préstamo (Enter = hoy): ").strip()
            persona.agregar_libro(libro, fecha or None)
            print(f"Libro '{libro}' prestado a {persona.nombre}.")
    elif opcion == "3":
        if not persona.libros_prestados():
            print(f"{persona.nombre} no tiene libros prestados.")
            return
        persona.visualizar_libros()
        libro = input("Nombre del libro que devuelve: ").strip()
        if persona.devolver_libro(libro):
            print(f"Libro '{libro}' devuelto.")
        else:
            print(f"{persona.nombre} no tiene prestado '{libro}'.")
    else:
        print("Opción no válida.")
