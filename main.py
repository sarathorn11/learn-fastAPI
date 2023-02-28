from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/")
async def main():
    return {'data': {'name':'Sarath'}}

@app.get("/about")
def about():
    return {'data':{'about'}}


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)