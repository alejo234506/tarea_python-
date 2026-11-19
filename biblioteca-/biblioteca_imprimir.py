"""Imprimir todos los usuarios de la biblioteca."""


def imprimir_todos(biblioteca: dict) -> None:
    if not biblioteca:
        print("La biblioteca no tiene usuarios todavía.")
        return
    print(f"Usuarios registrados: {len(biblioteca)}")
    for persona in biblioteca.values():
        print(persona)
        persona.visualizar_libros()
