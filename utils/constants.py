from uuid import uuid4
from .enums import Method
from random import randint

URI = "ws://0.0.0.0:8080"
ID = str(uuid4())
PHONE = str(randint(1000000, 9999999))