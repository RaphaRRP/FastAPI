from fastapi import FastAPI, HTTPException, status
from models import Curso
from typing import List, Optional

app = FastAPI()

cursos = {
    1: {
        "titulo": "Programção",
        "aulas": 112,
        "horas": 50
    },
    2: {
        "titulo": "Lógica",
        "aulas": 100,
        "horas": 30
    }
}

@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')
    
@app.post('/cursos')
async def post_curso(curso: Curso):
    if curso.id not in cursos:
        cursos[curso.id] = curso
        return curso
    else:
        raise HTTPException(status_code=409, defail=f'ja existe um curso com o ID {curso.id}.')


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)