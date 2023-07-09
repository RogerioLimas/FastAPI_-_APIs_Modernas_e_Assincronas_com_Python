from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def home():
    return {'msg': 'Hello!'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
