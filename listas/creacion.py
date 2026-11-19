"""Crea una lista de palabras y luego quita las que el usuario indique."""


def pedir_numero(mensaje: str) -> int:
    """Pide un número entero positivo y repite hasta que sea válido."""
    while True:
        try:
            numero = int(input(mensaje))
            if numero >= 0:
                return numero
            print("El número no puede ser negativo.")
        except ValueError:
            print("Eso no es un número, intenta otra vez.")


def pedir_palabras(cantidad: int, mensaje: str) -> list:
    palabras = []
    for i in range(cantidad):
        palabras.append(input(f"{mensaje} {i + 1}: ").strip())
    return palabras


def operacion_listas() -> list:
    cantidad = pedir_numero("Digita el número de palabras de la lista: ")
    lista = pedir_palabras(cantidad, "Digita la palabra")
    print("Lista:", lista)

    cantidad_quitar = pedir_numero("¿Cuántas palabras deseas quitar?: ")
    a_quitar = pedir_palabras(cantidad_quitar, "Digita la palabra que deseas quitar")

    for palabra in a_quitar:
        if palabra in lista:
            lista.remove(palabra)
        else:
            print(f"'{palabra}' no estaba en la lista")

    print("Lista final:", lista)
    return lista


if __name__ == "__main__":
    operacion_listas()
