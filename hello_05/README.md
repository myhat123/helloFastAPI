简化安全机制
==========

https://pypi.org/project/fastapi-login/

> $ pip install fastapi-login

```python
import os
print(os.urandom(32).hex())
```
> $ uvicorn main:app --reload

> $ http --form POST "http://127.0.0.1:8000/token" username='johndoe' password='secret'

> $ http -v --follow http://localhost:8000/users/me "accept: application/json" "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqb2huZG9lIiwiZXhwIjoxNjEwOTcyMTc2fQ.wlj5-NX6grISzzZwX_lL-InUektrjvRwmbuxywdQMD8"

> $ curl -X POST "http://localhost:8000/token" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "grant_type=&username=johndoe&password=secret&scope=&client_id=&client_secret="

> $ curl -X GET "http://localhost:8000/users/me/" -H  "accept: application/json" -H  "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqb2huZG9lIiwiZXhwIjoxNjEwOTczNjk0fQ.qtOfhY298TWh_TNQaWnqNqVU7nI7ZycPap9zwt9DJAg"