from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello World"}

# @app.get("/countries/{country_name}")
# async def country(country_name: str, city_name: str = 'tokyo'):
#     return {
#         "country_name": country_name,
#         "city_name": city_name
#     }

# @app.get("/countries/")
# async def country(country_name: Optional[str] = None, country_id: Optional[int] = None):
#     return {
#         "country_name": country_name,
#         "country_id": country_id
#     }

class ShopInfo(BaseModel):
    name: str
    location: str

class Item(BaseModel):
    name: str = Field(max_length=12)
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

class Data(BaseModel):
    shop_info: Optional[ShopInfo] = None
    items: List[Item]

@app.post("/item")
async def create_item(data: Data):
    return {"message": data}
