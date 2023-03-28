# FastAPI
## creacion del entorno virtual
1. instalar la libreria del entorno virtual ````pip install virtualenv````
2. creacion de entorno virtual ````python -m virtualenv [NOMBRE]````
3. verificacmos el python general````pip freeze````
4. Entro a entorno virtual (EN WINDOWS desde GIT-BASH) ````source venv/Scripts/activate```` y sale el nombre de mi entorno virtual en mi linea de comandos.
5. para ingresar a la pagina es  ````uvicorn entrypoint:app --reload```` con esto te sale en el servidor 

## INSTALAR FastAPI
1. instalacion de FastAPI ````pip install fastapi uvicorn````
2. creamos un nuevo archivo llamado ````entrypoint.py````y con python
   from fastapi from FastAPI

3. corremos nuestro servidor ```` uvicorn entrypoint:app --reload````


##  Metodos HTTP 


|metodo|accion DB|uso|
|--|--|--|
|POST|create|crear un registro en nuestroi backend o base|
|GET|Read|acceder,recuperar o leer informacion |
|PUT|Update|actualizar o editar  un registro nuevo  |
|DELETE|Delete|Eliminar un registro de nuestro backend |


## CREACION DE PRIMERA RUTA 

```` PYTHON
from pydantic  from BaseModel

@app.get("/")
def hello_world_check():
    return{
        "titulo":"biblioteca STEAM",
        "ver":"v0.0.1"
    }
....
