## FastAPI - UserAuth

A basic example of a FastAPI backend with User Signup and Login APIs.

### Signup

```POST /api/v1/auth/signup```

Body:

```json
{
    "email": "test01@test.com",
    "full_name": "Dev Tyagi",
    "password": "123456",
    "phone": "9999999999"
}
```

Response:

```json
{
    "email": "test01@test.com",
    "full_name": "Dev Tyagi",
    "phone": "9999999999",
    "id": "ecc7605c-8bac-47e3-95c8-76bd740fde22"
}
```


### Login

```POST /api/v1/auth/login```

Body:

```json
{
    "email": "test01@test.com",
    "password": "123456"
}
```

Response:

```json
{
    "user": {
        "email": "test01@test.com",
        "full_name": "Dev Tyagi",
        "phone": "9999999999",
        "id": "597bd664-c1dc-42a6-8a7c-ec17d810687c"
    },
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0MDFAdGVzdC5jb20iLCJleHAiOjE2OTM0MzIxNjl9.TTKFv-egsgaOGOm5a5zO0y2R6_vubIoBUqmaFcmmZIc"
}
```

### Test Route

```GET /hello/user```

Header:   
```Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0MDFAdGVzdC5jb20iLCJleHAiOjE2OTM0MzIxNjl9.TTKFv-egsgaOGOm5a5zO0y2R6_vubIoBUqmaFcmmZIc```

Response:
```json
{
    "message": "Hello Dev Tyagi"
}
```
