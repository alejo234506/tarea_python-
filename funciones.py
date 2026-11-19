"""Funciones con manejo de errores (try / except)."""


def dividir(a: float, b: float) -> float | str:
    """Divide a entre b y avisa si hay un error en vez de romper el programa."""
    try:
        return a / b
    except ZeroDivisionError:
        return "no se puede dividir entre cero"
    except TypeError:
        return "solo se pueden dividir números"
    except Exception as error:
        return f"hubo otro error: {error}"


if __name__ == "__main__":
    print(dividir(10, 2))      # 5.0
    print(dividir(1, 0))       # no se puede dividir entre cero
    print(dividir("1", 2))     # solo se pueden dividir números
