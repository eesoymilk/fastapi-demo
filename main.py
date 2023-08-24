from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None


items: list[Item] = [
    Item(name="apple", description="keep doctors away"),
    Item(name="mug", description="very delicate"),
    Item(name="green tea", description="sugar free!"),
]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items")
async def read_items() -> list[Item]:
    return items


@app.post("/items")
async def create_item(item: Item):
    index = len(item)
    print(f"creating new item: {item}")
    items.append(item)
    return {"item_id": index}


@app.get("/items/{id}")
async def read_item(id: int):
    try:
        return items[id]
    except IndexError:
        return {"message": f"item {id} does not exist"}
