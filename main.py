from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'zohaib'}}

@app.get('/name')
def name():
    return {"item_id": "hey "}

