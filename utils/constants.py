from uuid import uuid4
from .enums import Method
from random import randint

URI = "ws://0.0.0.0:8080"
ID = str(uuid4())
PHONE = str(randint(1000000, 9999999))

update_body = {
    "id": "sfda-11231-123-adfb",
    "method": Method.UPDATE,
    "name": "Chuck",
    "surname": "Dorris",
    "phone": "2128509",
    "age": 100500,
}

select_body = {
    "id": "sfda-11231-123-adfb",
    "method": Method.SELECT,
    "name": "Chuck",
    "surname": "Dorris",
}
