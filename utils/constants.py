from uuid import uuid4
from .enums import Method

URI = "ws://0.0.0.0:8080"
ID = uuid4()


add_body = {
    "id": "sfda-11231-123-adfb",
    "method": Method.ADD,
    "name": "Chuck",
    "surname": "Dorris",
    "phone": "2128509",
    "age": 100500
}

delete_doby = {
    "id": "sfda-11231-123-adfb",
    "method": Method.DELETE,
    "phone": "1234567",
}

update_body = {
    "id": "sfda-11231-123-adfb",
    "method": Method.UPDATE,
    "name": "Chuck",
    "surname": "Dorris",
    "phone": "2128509",
    "age": 100500
}

select_body = {
    "id": "sfda-11231-123-adfb",
    "method": Method.SELECT,
    "name": "Chuck",
    "surname": "Dorris",
}