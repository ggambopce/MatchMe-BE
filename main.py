from fastapi import FastAPI
from dotenv import load_dotenv
import os

# 환경변수 불러오기
load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI + GraphQL 서버 시작 준비 완료"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
