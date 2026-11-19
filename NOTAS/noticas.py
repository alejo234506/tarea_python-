"""Ejercicios de clases (programación orientada a objetos).

Ejecuta el archivo y elige un ejercicio del menú:
    py NOTAS/noticas.py
"""


def pedir_numero(mensaje: str, tipo: type = float, minimo: float | None = None) -> float:
    """Pide un número y repite hasta que sea válido."""
    while True:
        try:
            valor = tipo(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Eso no es un número válido, intenta otra vez.")


# ============================== 1. Coche ==============================
class Coche:
    """Un coche gasta 1 litro de gasolina por cada kilómetro que avanza."""

    def __init__(self, matricula: str, marca: str, kilometros: float, gasolina: float) -> None:
        self.matricula = matricula
        self.marca = marca
        self.kilometros = kilometros
        self.gasolina = gasolina

    def avanzar(self, km: float) -> bool:
        # Solo puede avanzar si le alcanza la gasolina
        if km <= self.gasolina:
            self.gasolina -= km
            self.kilometros += km
            return True
        print(f"No alcanza la gasolina: tienes {self.gasolina} y necesitas {km}.")
        return False

    def __str__(self) -> str:
        return (f"{self.marca} {self.matricula}: {self.kilometros} km recorridos, "
                f"{self.gasolina} litros de gasolina")


# ============================== 2. Robot ==============================
class Robot:
    """Un robot que se mueve en un plano (x, y)."""

    def __init__(self, nombre: str, x: int = 0, y: int = 0) -> None:
        self.nombre = nombre
        self.x = x
        self.y = y

    def arriba(self, n: int) -> None:
        self.y += n

    def abajo(self, n: int) -> None:
        self.y -= n

    def derecha(self, n: int) -> None:
        self.x += n

    def izquierda(self, n: int) -> None:
        self.x -= n

    def posicion(self) -> str:
        return f"{self.nombre} se encuentra en ({self.x}, {self.y})"


# ============================== 3. Alumno ==============================
class Alumno:
    """Gana el año si la nota es 3 o más (escala de 0 a 5)."""

    NOTA_MINIMA = 3.0

    def __init__(self, nombre: str, nota: float) -> None:
        self.nombre = nombre
        self.nota = nota

    def resultado(self) -> str:
        if self.nota >= self.NOTA_MINIMA:
            return f"{self.nombre} ganó el año con {self.nota}"
        return f"{self.nombre} perdió el año con {self.nota}"


# ============================== 4. Cuenta ==============================
class Cuenta:
    """Cuenta bancaria: se puede ingresar y retirar dinero, nunca quedar en negativo."""

    def __init__(self, titular: str, cantidad: float = 0) -> None:
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self) -> str:
        return f"La cuenta de {self.titular} tiene ${self.cantidad:,.0f}"

    def ingresar(self, valor: float) -> bool:
        if valor <= 0:
            print("El valor a ingresar debe ser mayor que cero.")
            return False
        self.cantidad += valor
        return True

    def retirar(self, valor: float) -> bool:
        if valor <= 0:
            print("El valor a retirar debe ser mayor que cero.")
            return False
        if valor > self.cantidad:
            print(f"Saldo insuficiente: solo tienes ${self.cantidad:,.0f}.")
            return False
        self.cantidad -= valor
        return True


# ============================== 5. Triángulo ==============================
class Triangulo:
    def __init__(self, nombre: str, a: float, b: float, c: float) -> None:
        self.nombre = nombre
        self.lados = [a, b, c]

    def es_valido(self) -> bool:
        """Desigualdad triangular: cada lado debe ser menor que la suma de los otros dos."""
        a, b, c = sorted(self.lados)
        return a > 0 and a + b > c

    def lado_mayor(self) -> float:
        return max(self.lados)

    def tipo_triangulo(self) -> str:
        if not self.es_valido():
            return "no es un triángulo válido"
        lados_distintos = len(set(self.lados))  # set() quita los repetidos
        if lados_distintos == 1:
            return "equilátero"
        if lados_distintos == 2:
            return "isósceles"
        return "escaleno"


# ============================== Menú interactivo ==============================
def ejercicio_coche() -> None:
    marca = input("Marca del coche: ") or "Chevrolet"
    matricula = input("Matrícula: ") or "QHY451"
    coche = Coche(matricula, marca, kilometros=0,
                  gasolina=pedir_numero("¿Cuántos litros de gasolina tiene?: ", minimo=0))
    km = pedir_numero("¿Cuántos km quieres avanzar?: ", minimo=0)
    coche.avanzar(km)
    print(coche)


def ejercicio_robot() -> None:
    robot = Robot(input("Nombre del robot: ") or "chechiño")
    movimientos = {"w": robot.arriba, "s": robot.abajo, "d": robot.derecha, "a": robot.izquierda}
    while True:
        print(robot.posicion())
        opcion = input("Mover: [w] arriba  [s] abajo  [d] derecha  [a] izquierda  [q] salir: ").lower()
        if opcion == "q":
            break
        if opcion in movimientos:
            movimientos[opcion](pedir_numero("¿Cuántos puntos?: ", int, minimo=0))
        else:
            print("Opción no válida.")


def ejercicio_alumno() -> None:
    nombre = input("Nombre del alumno: ") or "Alumno"
    nota = pedir_numero("¿Cuánto sacaste? (0 a 5): ", minimo=0)
    print(Alumno(nombre, nota).resultado())


def ejercicio_cuenta() -> None:
    cuenta = Cuenta(input("Titular de la cuenta: ") or "Titular")
    while True:
        print(cuenta.mostrar())
        opcion = input("[1] ingresar  [2] retirar  [3] salir: ")
        if opcion == "1":
            cuenta.ingresar(pedir_numero("Cantidad a depositar: "))
        elif opcion == "2":
            cuenta.retirar(pedir_numero("Cantidad a retirar: "))
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")


def ejercicio_triangulo() -> None:
    lados = [pedir_numero(f"Introduce el lado {letra}: ", minimo=0) for letra in "abc"]
    tri = Triangulo("triangulito", *lados)
    print(f"El lado mayor es {tri.lado_mayor()}")
    print(f"El triángulo es {tri.tipo_triangulo()}")


def menu() -> None:
    ejercicios = {
        "1": ("Coche", ejercicio_coche),
        "2": ("Robot", ejercicio_robot),
        "3": ("Alumno", ejercicio_alumno),
        "4": ("Cuenta bancaria", ejercicio_cuenta),
        "5": ("Triángulo", ejercicio_triangulo),
    }
    while True:
        print("\n" + "=" * 40)
        for clave, (nombre, _) in ejercicios.items():
            print(f"  [{clave}] {nombre}")
        print("  [0] Salir")
        opcion = input("Elige un ejercicio: ")
        if opcion == "0":
            break
        if opcion in ejercicios:
            ejercicios[opcion][1]()
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
