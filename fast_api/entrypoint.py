from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os 

# cargamos el entorno virtual
NAME = os.getenv("NAME")
VERSION = os.getenv("VERSION")
print(NAME,VERSION)

servidor = FastAPI(
    title=NAME,
    version=VERSION
)





#registramos una funcion en mi app o en una ruta (endpoint)
# '/' ruta raiz 
# solo podemos tener una funcion por verbo en una ruta 







# @app.get("/corre/{nombre}")
# def Dios (nombre):
#     return  f"corre por que si no mueres  {nombre}"




# @app.get("/activo/{nombre}")
# def reniga(nombre):
#     return f"estas modo activo, por eso dame comida  {nombre} "


# @app.get("/me_caes_bien/{nombre}")
# def melo (nombre):
#     return f"estas re nea {nombre}"


# @app.get("/g/{nombre}")
# def hambre(nombre):
#     return f"dame comida {nombre}"

# @app.get("/hola/{nombre}/{edad}")
# def hola(nombre:str,edad:int):
#     if  edad<18:
#         return f"hola {nombre} , {edad} eres menor de edad "
#     else :
#         return f"hola {nombre} , {edad} eres mayor de edad  "

# @app.get("/cuadrado/{lado}")
# def hola(lado:int):
#     z = lado * lado
#     return f"que mas el valor de tu cuadrado es {z}"
# @app.get("/{id}")
# def usuario(id:str):
#     return biblioteca[id]

# @app.get("/{id}/{id_libro}")
# def usuario(id :str,id_libro:str):
    
#     return biblioteca [id]["libros"][id_libro]  

 
biblioteca = []
     
#<!-- "1":{
#         "nombre":"alejandro ",
#         "edad":"16",
#         "libros":{
#         "1":{
#             "libro":"5am",
#             "fecha":"13/3/2023",
#             "estado":"prestado"
#         },
#         "2":{
#             "libro":"100 años de soledad",
#             "fecha":"13/5/2023",
#             "estado":"prestado"
#         },
#         }
        
#     },
#  >   "2":{
#         "nombre":"valery",
#         "edad":"17",
#         "libros":{
            
#             "1": {
#               "libro":"habtios de la vida",
#               "fecha":"14/3/2023",
#               "estado":"prestado"
#             },
#             "2" :{
#             "libro":"poesia y mitos",
#             "fecha":"13/5/2023",
#             "estado":"prestado"
#             },
#         }
            
    #     } --]
# @app.get("/")
# def hello_world_check():
#     return{
#         "titulo":"biblioteca STEAM",
#         "ver":"v0.0.1"
#     }
    
@app.get("/personas")
def personas_all():
    return biblioteca 

# @app.get("/personas/{id}")
# def hello_world_check(id:str):
#     return biblioteca[id]

class personaBiblioteca(BaseModel):
     id:str
     nombre:str
     edad:int
     libros:dict
@servidor.post("/personas")
def personas_add(request:personaBiblioteca):
    biblioteca.update(request)
    return request 

class personabiblioteca(BaseModel):
     id:str
     nombre:str
     edad:int
     libros:dict
@servidor.post("/personas")
def personas_add(request:personaBiblioteca):
    biblioteca.update(request)
    return request

class PersonaModify(BaseModel):
     id:str
     nombre:str
     edad:int
     libros:dict
@servidor.put("/personas")
def personas_modify(request:PersonaModify):
    for i in biblioteca:
        if i.id==id:
            i.nombre=request.nombre
            i.edad=request.edad
            return i
    return {"error":"persona no encontrada"}


@servidor.delete("/personas/{id}")
def personas_delete(id:str):
    for i in biblioteca:
        print(i)
        if i.id==id:
         print(i.id)
 

@servidor.get("/")
def suma(a:float,b:float) -> float:
    try:
      return(a/b)
    except ZeroDivisionError:
        return("no se puede dividir entre cero ")
    except TypeError:
        return("no se puede dividir entre cero ")
    except exception:
        return("hubo otro error")
    

    


    







             






     
