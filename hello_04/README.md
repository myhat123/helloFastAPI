安全机制
=======

JWT == JSON Web Tokens

> $ pip install python-jose[cryptography]

python-jose 生成 jwt

passlib包用来处理 Password hashing 密码，不用明码

> $ pip install passlib[bcrypt]

生成随机密钥SECRET_KEY

> $ openssl rand -hex 32

> $ uvicorn main:app --reload

用户: johndoe 密码: secret，密码对应的hash: $2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW

> $ curl -X POST "http://localhost:8000/token" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "grant_type=&username=johndoe&password=secret&scope=&client_id=&client_secret="

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huZG9lIiwiZXhwIjoxNjEwODc5MjIyfQ.F-XO2YWe8bmDeGsC4GLWhN-4gTuvQ1_6ZIoYlh1Ze8s",
  "token_type": "bearer"
}
```

> $ curl -v -X GET "http://localhost:8000/users/me/" -H  "accept: application/json" -H  "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huZG9lIiwiZXhwIjoxNjEwODkwNTY1fQ.KC_kI8iufsN00RKso905bhRiKgGPnmIKJeOC1ueZoIM"

http --form POST "http://127.0.0.1:8000/token" username='johndoe' password='secret'

http -v --follow http://localhost:8000/users/me "accept: application/json" "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huZG9lIiwiZXhwIjoxNjEwODkwNTY1fQ.KC_kI8iufsN00RKso905bhRiKgGPnmIKJeOC1ueZoIM"

expired说明
==========

过期时间，存疑，时间是放到要生成的token里

时间使用，datetime.utcnow()，utc需要改变

加密
===

get_password_hash 生成随机的password hash，每次生成不同

>>> import main
>>> main.get_password_hash("secret")
'$2b$12$WbtCia6fG71PJ.g/jrXLReLcUyJS2.d5S6DTroX7fzn9/3uGx7h5a'
>>> 
