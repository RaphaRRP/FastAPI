from fastapi import FastAPI, HTTPException, status, Path, Query, Header, Depends
from fastapi.responses import JSONResponse
from models import Curso
from typing import List, Optional, Any, Dict
from time import sleep
from models import cursos


def fake_db():
    try:
        print('Abrindo conexão com bancos de dados...')
        sleep(1)
    finally:
        print('Fechando conexão com bancos de dados...')
        sleep(1)     


app = FastAPI(
    title='Documentação',
    version='0.0.1',
    description='Api sobre fast api'
    )




@app.get('/cursos', 
        description='retorna os cursos',
        summary='retorna os cursos',
        response_model=Dict[int, Curso])
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int = Path(default=None, title='ID do curso', description='Deve ser entre 1 e 2 ', gt=0, lt=3), db: Any = Depends(fake_db)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')
    
@app.post('/cursos', status_code=201)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    next_id: int = len(cursos) + 1
    curso.id = next.id
    curso.append(curso)
    return curso


@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    

@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        del cursos[curso_id]
        return JSONResponse(status_code=204)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')
    
@app.get('/calculadora')
async def calcular(a: int = Query(default=None, gt=5), b: int = Query(default=None, gt=10), c: Optional[int] = None, x_geek: str = Header(default=None)):
    resultado = a + b 

    if c:
        resultado += c

    print(f'x_geek: {x_geek}')

    return {'resultado': resultado}
    


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)