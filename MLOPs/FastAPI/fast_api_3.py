from typing import Annotated

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()

items = [
    {
        "name": "Banh thap cam",
        "price": 30000,
        "description": "A traditional Vietnamese dessert made with layers of colorful ingredients.",
    },
    {
        "name": "Che ba mau",
        "price": 25000,
        "description": "A popular Vietnamese dessert consisting of three layers: mung bean paste, red beans, and pandan jelly, topped with coconut milk.",
    },
]

class Item(BaseModel):
    name: str = Field(..., example="Banh thap cam", min_length=3, max_length=100)
    price: float = Field(..., example=30000, description="Price in VND", gt=0)
    description: str | None = Field(None, max_length = 500, example="A traditional Vietnamese dessert made with layers of colorful ingredients.", description="Detailed description of the item")


    @app.get("/search_items/")
    async def search_items(q: Annotated[str, Query(min_length=3, max_length=50, description = "Search Query")], max_price : Annotated[float | None, Query(gt=0, description = "Maximum Price")] = None):
        results = [item for item in items if q.lower() in item["name"].lower()]

        if max_price:
            results = [item for item in results if item["price"] <= max_price]

        return results