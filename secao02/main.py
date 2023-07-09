from fastapi import FastAPI

app = FastAPI()


@app.get("/msg")
async def mensagem():
    return {'msg': 'FastAPI na Geek University'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='localhost', port=8000,
                reload=True, log_level='info')
