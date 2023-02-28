
biblioteca={}

def agregar_usuario(diccionario:dict) -> dict:
    nombre=input('cual es tu nombre?:')
    libro=input('cual es el libro que presto:')
    fecha_de_prestamo=input('que dia lo prestaste:')
    
    diccionario_interno ={
        'libro':libro, 
        'fecha':fecha_de_prestamo
    }
    print(diccionario_interno)
    
    
    if  diccionario.get(nombre) ==None:
      
       diccionario[nombre]=(diccionario_interno)
    else:  
       diccionario[nombre].append(diccionario_interno)
    #diccionario[nombre]
    print(diccionario)
agregar_usuario(biblioteca)
    
    
    