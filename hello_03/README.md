初步安全机制
==========

> $ uvicorn main:app --reload

> $ curl -X POST "http://localhost:8000/token" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "grant_type=&username=johndoe&password=secret&scope=&client_id=&client_secret="

> $ curl -X GET "http://localhost:8000/users/me" -H  "accept: application/json" -H  "Authorization: Bearer johndoe"

> $ http --form POST "http://127.0.0.1:8000/token" username='johndoe' password='secret'

> $ http http://localhost:8000/users/me "Authorization:Bearer johndoe"