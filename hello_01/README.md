FastAPI入门
===========

> $ pip install fastapi

> $ pip install uvicorn[standard]

运行
===

> $ uvicorn main:app --reload

代码
===

```python
@app.get("/")
async def root():
    return {"message": "Hello World"}
```

async/await 是python 3.6才有的语言特性

api doc
=======

http://localhost:8000/docs

http://localhost:8000/redoc

检查类型
=======

```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

http://localhost:8000/items/foo
http://localhost:8000/items/4.2

类型不匹配

pydantic
========

数据有效性