"""Herencia: Persona, Gato y Perro heredan de SerVivo y cambian su comportamiento."""


class SerVivo:
    sentidos_lista = ["olfato", "vista", "tacto", "gusto", "oído"]

    def __init__(self, nombre):
        self.nombre = nombre

    def sentidos(self):
        print(f"{self.nombre} tiene estos sentidos: {', '.join(self.sentidos_lista)}")

    def movimiento(self):
        print(f"{self.nombre} se está moviendo")

    def sonido(self):
        print(f"{self.nombre} está haciendo un sonido")


# Las clases hijas heredan sentidos() tal cual y solo cambian lo que es distinto
class Persona(SerVivo):
    def movimiento(self):
        print(f"{self.nombre} está construyendo como Bob el constructor")

    def sonido(self):
        print(f"{self.nombre} está hablando")


class Gato(SerVivo):
    def movimiento(self):
        print(f"{self.nombre} está construyendo una arena de golf")

    def sonido(self):
        print(f"{self.nombre} está maullando")


class Perro(SerVivo):
    def movimiento(self):
        print(f"{self.nombre} está mordiendo a otro")

    def sonido(self):
        print(f"{self.nombre} está ladrando")


if __name__ == "__main__":
    seres = [Persona("Kemba Walker"), Gato("Michi"), Perro("Firulais")]
    for ser in seres:
        ser.sentidos()
        ser.movimiento()
        ser.sonido()
        print("-" * 40)
