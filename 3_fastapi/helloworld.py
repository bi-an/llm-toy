from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def home():
    return {"user_id": 123}

@app.get("/shop")
async def shop():
    return {"商品信息": "..."}


if __name__ == '__main__':
    uvicorn.run(
        "helloworld:app",
        port = 8080,
        reload = True
    )
