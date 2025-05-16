from fastapi import FastAPI, HTTPException

app = FastAPI()
items = {}

@app.post("/items/{item_id}")
def create_item(item_id: int, name: str):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = name
    return {"item_id": item_id, "name": name}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "name": items[item_id]}