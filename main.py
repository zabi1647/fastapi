from fastapi import FastAPI
from typing import Optional
import item_data as item



app = FastAPI()



@app.get('/')
def index():
    print("this is index")
    return {'data':{'name':'Ali'}}

@app.get('/hello')
def he(published : bool = False,limit = 10, sort: Optional[str] = "Malik"):
    if published:
      return {'data':{'blog':f'blog list {limit} and published {published} and sort {sort}'}}
    else:
        return {'data':{'blog':'not publishe'}}

@app.get('/test/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/test/{id}')
def test(id: int):
    return {'message': id}


@app.post('/create')
def createBlog(item: item.Item):
    return {'data':{'name':item.name,'description':item.description}}
  


