
from typing import Optional
from pydantic import BaseModel

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int


cursos = [
    Curso(titulo = "Programção", aulas= 112, horas= 50),
    Curso(titulo = "Lógica", aulas = 100, horas = 30),
]