from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def 작명():
    return 'hello'

@app.get("/data")
def 작명():
    return {'hello' : 1234}


from pydantic import BaseModel
class Model(BaseModel):
    name :str
    phone :int

#비동기 처리 가능

@app.post("/send")
def 작명(data : Model):
    print(data)
    return '전송완료'