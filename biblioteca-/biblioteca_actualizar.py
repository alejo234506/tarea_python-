def actualizar_usuario(dataset: list) -> list:
    dato1 = input("ingrese viejo dato actualizar:")
    dato2 = input("ingrese nuevo dato actualizar:")
    dataset.remove(dato1)
    dataset.append(dato2)