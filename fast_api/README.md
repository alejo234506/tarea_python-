# FastAPI – Biblioteca STEAM

## Creación del entorno virtual
1. Crear el entorno virtual: `py -m venv venv`
2. Entrar al entorno virtual:
   - Git Bash: `source venv/Scripts/activate`
   - PowerShell: `venv\Scripts\Activate.ps1`

   Sale `(venv)` al inicio de la línea de comandos.
3. Ver lo que hay instalado: `pip freeze`

## Instalar FastAPI
```bash
pip install -r requirements.txt
```
Esto instala `fastapi`, `uvicorn` y `python-dotenv`.

## Correr el servidor
Desde la carpeta `fast_api`:
```bash
uvicorn entrypoint:app --reload
```
- API: http://127.0.0.1:8000
- Documentación interactiva para probar todo: http://127.0.0.1:8000/docs

El nombre y la versión del servidor salen del archivo `.env` de la carpeta principal (`NAME` y `VERSION`). Ese archivo no se sube al repositorio: cópialo desde `.env.example` (`cp ../.env.example ../.env`).

## Métodos HTTP

| Método | Acción DB | Uso |
|--|--|--|
| POST | Create | crear un registro en nuestro backend o base |
| GET | Read | acceder, recuperar o leer información |
| PUT | Update | actualizar o editar un registro |
| DELETE | Delete | eliminar un registro de nuestro backend |

## Rutas de la API

| Método | Ruta | Qué hace |
|--|--|--|
| GET | `/` | información del servidor |
| GET | `/personas` | lista todas las personas |
| GET | `/personas/{id}` | una persona |
| POST | `/personas` | crea una persona (409 si el id ya existe) |
| PUT | `/personas/{id}` | cambia nombre y/o edad |
| DELETE | `/personas/{id}` | elimina una persona |
| GET | `/personas/{id}/libros` | libros de una persona |
| GET | `/personas/{id}/libros/{numero}` | un libro (empieza en 1) |
| POST | `/personas/{id}/libros` | presta un libro a la persona |
| PUT | `/personas/{id}/libros/{numero}/devolver` | marca el libro como devuelto |
| GET | `/dividir?a=10&b=2` | divide (400 si `b` es 0) |
| GET | `/hola/{nombre}/{edad}` | dice si es mayor o menor de edad |
| GET | `/cuadrado/{lado}` | área de un cuadrado |

Si algo no existe, la API responde **404**; si los datos están mal (por ejemplo, edad negativa), responde **422**.

### Ejemplo para crear una persona (POST `/personas`)
```json
{
  "id": "3",
  "nombre": "sergio",
  "edad": 20,
  "libros": [
    { "nombre": "Cien años de soledad", "fecha": "18/11/2026" }
  ]
}
```

## Primera ruta (ejemplo básico)
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world_check():
    return {"titulo": "biblioteca STEAM", "ver": "v0.0.1"}
```

> Los datos se guardan en memoria: al reiniciar el servidor vuelven a quedar las dos personas de ejemplo.
