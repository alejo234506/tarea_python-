"""Práctica de listas: agregar, ordenar, rebanar (slicing) y range."""

listas = [1, 2, 3, 4]


def funciones(parametro):
    """Agrega el parámetro a la lista y devuelve el doble del parámetro."""
    print(parametro)
    listas.append(parametro)
    variable = parametro * 2
    print(listas)
    return variable


print(funciones(5))  # agrega 5 a la lista y muestra 10

# Una lista puede guardar datos de distintos tipos
mezcla = ['string', 1, 2.4, True]
print(mezcla)
# mezcla.pop()          -> quita el último elemento
# mezcla.append(valor)  -> agrega un elemento al final
# mezcla.remove(valor)  -> quita el primer elemento igual a valor

nombres = ["felipe", "gabriela", "juan", "perez", "david"]
nombres.sort(reverse=False)  # orden alfabético
print(nombres)

# Rebanada [inicio:fin:paso] -> desde la posición 1 hasta la 4, saltando de 2 en 2
print(nombres[1:5:2])

# range(inicio, fin, paso)
for i in range(3, 10, 2):
    print(i)

print(list(range(3, 10)))  # range se convierte en lista para poder verlo
