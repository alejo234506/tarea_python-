import datetime

biblioteca={}

def agregar_usuario(diccionario:dict) -> dict:
    nombre=input('cual es tu nombre?:')
    libro=input('cual es el libro que presto:')
    fecha =datetime.datetime.now()
    fecha_de_prestamo=(input('que dia lo prestaste'))
    
    diccionario_interno ={
        'libro':libro, 
        'fecha':fecha 
    }
    
    print(diccionario_interno)
    
    diccionario[nombre]=()
    
    print(diccionario)


agregar_usuario(biblioteca)