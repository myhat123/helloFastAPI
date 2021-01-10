发送数据
=======

A request body is data sent by the client to your API. A response body is the data your API sends to the client.

request body <==> response body

为了声明 request body, 使用Pydantic models

http://localhost:8000/docs

> $ curl -X POST "http://127.0.0.1:8000/items/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"Foo\",\"price\":45.2}"

> $ pip install httpie

字符串 name='Foo'，其他类型 := 

> $ http POST "http://127.0.0.1:8000/items/" name='Foo' price:=45.2