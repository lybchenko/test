from fastapi import FastAPI
from models import UserCreate, sample_products

app = FastAPI()


@app.get('/product/{product_id}')
async def func_3_16_1(product_id: int):
    for i in sample_products:
        if i['product_id'] == product_id:
            return i
        
    return 'Не найдено'


@app.get('/products/search')
async def func_3_16_2(keyword: str,category: str | None = None, limit: int = 10):
    pass




@app.post('/create_user')
def func(user: UserCreate):
    return 'find user:', user