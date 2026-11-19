# Tareas de Python

Ejercicios de Python: funciones, listas, clases, herencia, una biblioteca en consola y una API con FastAPI.

> En Windows usa `py` (o `python` si lo tienes configurado).

| Archivo | Tema | Cómo ejecutarlo |
|--|--|--|
| `funciones.py` | División con manejo de errores (`try/except`) | `py funciones.py` |
| `listas.py` | Listas: agregar, ordenar, rebanar, `range` | `py listas.py` |
| `listas/creacion.py` | Crear una lista de palabras y quitar algunas | `py listas/creacion.py` |
| `hereditario.py` | Herencia: Persona, Gato y Perro heredan de SerVivo | `py hereditario.py` |
| `NOTAS/noticas.py` | Clases: Coche, Robot, Alumno, Cuenta bancaria y Triángulo (con menú) | `py NOTAS/noticas.py` |
| `biblioteca-/biblioteca.py` | Biblioteca en consola: crear, actualizar, ver y eliminar usuarios y préstamos de libros | `py biblioteca-/biblioteca.py` |
| `fast_api/entrypoint.py` | API REST de la biblioteca con FastAPI | ver [fast_api/README.md](fast_api/README.md) |
| `mando.md` | Apuntes de comandos de terminal y git | — |

## Biblioteca en consola
Los archivos de `biblioteca-/` trabajan juntos:

- `biblioteca.py`: el menú principal. Guarda los datos en `biblioteca.json`, así no se pierden al cerrar.
- `biblioteca_crear.py`: la clase `Persona` y la creación de usuarios.
- `biblioteca_actualizar.py`: cambiar el nombre, prestar o devolver libros.
- `biblioteca_visualizar.py`: buscar y ver un usuario.
- `biblioteca_imprimir.py`: ver todos los usuarios.
- `biblioteca_remover.py`: eliminar un usuario (pide confirmación).

## API con FastAPI
```bash
cd fast_api
py -m venv venv
source venv/Scripts/activate      # Git Bash  (PowerShell: venv\Scripts\Activate.ps1)
pip install -r requirements.txt
uvicorn entrypoint:app --reload
```
Abre http://127.0.0.1:8000/docs para probar todas las rutas desde el navegador.
