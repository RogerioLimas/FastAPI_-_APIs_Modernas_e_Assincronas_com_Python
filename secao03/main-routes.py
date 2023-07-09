from fastapi import FastAPI, routing
import uvicorn

from routes import cursos_router, usuario_router


app = FastAPI()
app.include_router(cursos_router.router, tags=['cursos'])
app.include_router(usuario_router.router, tags=['usuarios'])

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
