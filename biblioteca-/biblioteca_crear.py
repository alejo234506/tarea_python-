# #este programa te dice el libro que quieres adquirir en una biblioteca con tu nombre
# from biblioteca_crear  import * 
# from biblioteca_actualizar import *

# bili={}

# while True:
#    print("*"*70)
#    menu = int(input("""Este menu es para oder adquirir un libro en una biblioteca 
#       [0]  crear un usuario nuevo 
#       [1]  actualizar el usuario
#       [2]  visualizar el usuario
#       [3]  eliminar el usuario
#       [4]  cerrar 
#       -INGRESA EL NUMERO:
#       """))
#       if menu == 0:
#       agregar_usuario(bili)
#     elif menu == 1:
#       actualizar_usuario(bili)
#     elif menu == 2:
#       print(bili)
#     elif  menu == 3:
#      eliminar_usuario(bili)
#     elif  menu == 4:
#       break
#    print("-"*50)
# 


class Persona():
    def __init__(self,id,nombre):
        self.id = id
        self.nombre = nombre
        self.info = {
            "id": self.id,
            "nombre": self.nombre,
            "libros":
                []
        }
    
    def __str__(self):
        cantidad_libros = len(self.info["libros"])
        return f"{self.id}:{self.nombre} = tiene {cantidad_libros} prestados"
    
    def agregar_libro(self,libro,fecha):
        libro_prestado = {
            "nombre":libro,
            "fecha":fecha,
            "estado":"prestado"
        }
        self.info["libros"].append(libro_prestado)
        
    def visualizar_libros(self):
        print(self.info["libros"])
    
    def devolver_libro(self,libro):
        for i in self.info["libros"]:
            if i["nombre"] == libro:
                print("si está")
                i["estado"] = "devuelto"
            

p1 = Persona("1","ernesto ")
print(p1)
p1.agregar_libro("1","1")
p1.agregar_libro("2","2")
p1.agregar_libro("3","3")
print(p1)
p1.visualizar_libros()
p1.devolver_libro("1")
p1.visualizar_libros()