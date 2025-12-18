from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Annotated,Literal

fast = FastAPI()
# general api
"""@fast.get("/item/{item_id}")
async def read_root(item_id: int):
    return {"items": f"HI!, Guys {item_id}"}

read_root(10)"""
# query parameter
# for accesing the result: http://http://127.0.0.1:8000/item/4?q=vinoth&short=1, ?-seperator(tells path is over),& is used for telling we have multiple parameter.
"""@fast.get("/item/{item_id}")
async def update_item(item_id: int, q: str | None=None, short: bool = False):
    item = {"item_id": "This is my first FastAPI app!"}
    if q:
        item.update({q: 'hope you are doing great!'})
    if short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item
    
print(update_item(item_id=4,q="vinoth", short=True))"""
"""
#send request to the api
# for input we have to go to the url: http://http://127.0.0.1:8000/docs and click of the path(here it is item) and then click on try it out button and give the input in json format and click on execute button.
from pydantic import BaseModel #used for data validation
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
@fast.post('/item')
async def sample_item(item: Item):
    if item.tax and not item.description:
        price_with_tax = item.price + item.tax
        return f"hi!, item is {item.name} and item have taxt and price + tax is {price_with_tax}"
    if item.description and item.tax:
        return f"hi!, item is {item.name} with price {item.price+item.tax} and item description is {item.description}"
    if item.description:
        return f"hi!, item is {item.name} with item price {item.price} and description is {item.description}"
    if item.name and item.price:
        return f"hi!, item is{item.name} with item price is {item.price}"""

#query parameter

"""class valid_data(BaseModel):
    name : str = Field(min_length=3, max_length=50)
    age : int = Field(gt=0,lt=100)
    model : Literal['Linear','Logistic','DecisionTree']= 'Linear'
    tags: list[str] = []

@fast.get("/validate/")
async def validate_data(data: Annotated[valid_data, Query()]): # annotated is used to add metadata to the pydantic model, which expect data to be Annotated[type, metadata]metadata-query,header,body,path
    return data
"""

@fast.get('/')
async def hello():
    return 'hi there! welcome to FastAPI'