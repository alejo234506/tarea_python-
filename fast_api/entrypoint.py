"""API de la biblioteca STEAM hecha con FastAPI.

Ejecutar (desde la carpeta fast_api):
    uvicorn entrypoint:app --reload
Documentación interactiva: http://127.0.0.1:8000/docs
"""
import os
from pathlib import Path
from typing import Literal

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

# Cargamos las variables del archivo .env (está en la carpeta principal del proyecto)
load_dotenv(Path(__file__).resolve().parent.parent / ".env")
NAME = os.getenv("NAME", "biblioteca STEAM")
VERSION = os.getenv("VERSION", "v0.1.0")

app = FastAPI(title=NAME, version=VERSION)


# ============================== Modelos ==============================
class Libro(BaseModel):
    nombre: str = Field(min_length=1)
    fecha: str = Field(examples=["13/03/2023"])
    estado: Literal["prestado", "devuelto"] = "prestado"


class Persona(BaseModel):
    id: str = Field(min_length=1)
    nombre: str = Field(min_length=1)
    edad: int = Field(ge=0, le=120)
    libros: list[Libro] = []


class PersonaModificar(BaseModel):
    """Para el PUT: solo se cambian los campos que se envían."""
    nombre: str | None = Field(default=None, min_length=1)
    edad: int | None = Field(default=None, ge=0, le=120)


# ============================== Datos ==============================
# La biblioteca vive en memoria: un diccionario {id: Persona}
biblioteca: dict[str, Persona] = {
    "1": Persona(id="1", nombre="alejandro", edad=16, libros=[
        Libro(nombre="5am", fecha="13/03/2023"),
        Libro(nombre="100 años de soledad", fecha="13/05/2023"),
    ]),
    "2": Persona(id="2", nombre="valery", edad=17, libros=[
        Libro(nombre="hábitos de la vida", fecha="14/03/2023"),
        Libro(nombre="poesía y mitos", fecha="13/05/2023"),
    ]),
}


def obtener_persona(id: str) -> Persona:
    persona = biblioteca.get(id)
    if persona is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"persona {id} no encontrada")
    return persona


# ============================== Rutas ==============================
@app.get("/")
def inicio():
    return {"titulo": NAME, "version": VERSION, "documentacion": "/docs"}


# ----- CRUD de personas -----
@app.get("/personas")
def personas_todas() -> list[Persona]:
    return list(biblioteca.values())


@app.get("/personas/{id}")
def persona_una(id: str) -> Persona:
    return obtener_persona(id)


@app.post("/personas", status_code=status.HTTP_201_CREATED)
def personas_agregar(persona: Persona) -> Persona:
    if persona.id in biblioteca:
        raise HTTPException(status.HTTP_409_CONFLICT, f"ya existe una persona con id {persona.id}")
    biblioteca[persona.id] = persona
    return persona


@app.put("/personas/{id}")
def personas_modificar(id: str, cambios: PersonaModificar) -> Persona:
    persona = obtener_persona(id)
    if cambios.nombre is not None:
        persona.nombre = cambios.nombre
    if cambios.edad is not None:
        persona.edad = cambios.edad
    return persona


@app.delete("/personas/{id}")
def personas_eliminar(id: str):
    persona = obtener_persona(id)
    del biblioteca[id]
    return {"mensaje": f"{persona.nombre} fue eliminado(a) de la biblioteca"}


# ----- Libros de una persona -----
@app.get("/personas/{id}/libros")
def libros_de_persona(id: str) -> list[Libro]:
    return obtener_persona(id).libros


@app.get("/personas/{id}/libros/{numero}")
def libro_de_persona(id: str, numero: int) -> Libro:
    """numero empieza en 1 (el primer libro es el 1)."""
    libros = obtener_persona(id).libros
    if not 1 <= numero <= len(libros):
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"la persona {id} no tiene el libro {numero}")
    return libros[numero - 1]


@app.post("/personas/{id}/libros", status_code=status.HTTP_201_CREATED)
def prestar_libro(id: str, libro: Libro) -> Persona:
    persona = obtener_persona(id)
    persona.libros.append(libro)
    return persona


@app.put("/personas/{id}/libros/{numero}/devolver")
def devolver_libro(id: str, numero: int) -> Libro:
    libro = libro_de_persona(id, numero)
    if libro.estado == "devuelto":
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "ese libro ya fue devuelto")
    libro.estado = "devuelto"
    return libro


# ----- Rutas de práctica -----
@app.get("/dividir")
def dividir(a: float, b: float):
    """Ejemplo: /dividir?a=10&b=2"""
    if b == 0:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "no se puede dividir entre cero")
    return {"a": a, "b": b, "resultado": a / b}


@app.get("/hola/{nombre}/{edad}")
def hola(nombre: str, edad: int):
    if edad < 18:
        return {"mensaje": f"hola {nombre}, con {edad} años eres menor de edad"}
    return {"mensaje": f"hola {nombre}, con {edad} años eres mayor de edad"}


@app.get("/cuadrado/{lado}")
def cuadrado(lado: float):
    return {"lado": lado, "area": lado * lado}
