from fastapi import FastAPI, HTTPException, status

app = FastAPI()
items = []
items_id = 1

@app.get('/')
def root():
    return {'message': 'Hello FastApi'}

@app.get('/items')
def get_item(item_id):
    try:
        return items[item_id - 1]
    except IndexError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='item does not exist')

@app.post('/items')
def create_item(name, coast, in_stock):
    global items_id
    item = {
        'id': items_id,
        'name': name,
        'coast': coast,
        'in_stock': in_stock
    }
    items.append(item)
    items_id += 1
    return item

@app.get('/ping')
def ping():
    return {"message": "pong"}
