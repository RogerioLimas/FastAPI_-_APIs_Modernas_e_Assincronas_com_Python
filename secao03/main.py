from typing import Annotated, Any, Optional
from fastapi import FastAPI, HTTPException, Header, status, Response, Path, Depends
from time import sleep

from models import Curso, cursos

app = FastAPI(
    title='API de Cursos da Geek University',
    version="2.3",
    description='Uma API para estudo do FastAPI')


def fake_db():
    try:
        print('Abrindo banco de dados')
        # sleep(1)
    finally:
        print('Fechando banco de dados')
        # sleep(1)


def find_curso(curso_id):
    return next((curso for curso in cursos if curso.id == curso_id), None)


@app.get('/cursos',
         description='Retorna todos os cursos ou uma lista vazia',
         summary='Retorna todos os cursos',
         response_description='Cursos retornados com sucesso!')
async def get_cursos(db: Any = Depends(fake_db)) -> list[Curso]:
    return cursos


@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int = Path(title='ID do curso',
                                         description='Deve ser entre 1 e 2', gt=0, lt=3)):
    curso = find_curso(curso_id)

    if not curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Curso '{curso_id}' não encontrado")
    return curso


@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso) -> list[Curso]:
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos.append(curso)
    return cursos


@app.put('/cursos/{curso_id}', status_code=status.HTTP_202_ACCEPTED)
async def put_curso(curso_id: int, curso: Curso) -> list[Curso]:
    found_curso = False

    for i in range(len(cursos)):
        if cursos[i].id == curso_id:
            found_curso = True
            cursos[i] = curso

    if not found_curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Não existe um curso com o id '{curso_id}'")
    return cursos


@app.delete('/cursos/{curso_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(curso_id: int) -> Response:
    curso = find_curso(curso_id)
    if not curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Curso '{curso_id}' não encontrado")
    cursos.remove(curso)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.get('/calculadora')
async def calculador(a: int, b: int, c: int, x_geek: str | None = Header(default=None)):
    resultado = a + b + c
    return {"resultado": resultado, "header": x_geek}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='localhost', port=8000,
                reload=True, log_level='info')
