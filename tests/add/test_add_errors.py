import json

import pytest
import websockets

from utils.constants import ID, PHONE, URI
from utils.enums import Status
from utils.helpers import get_modified_body
from utils.verifications import check_only_status

from .add_data import (add_body, empty_age, empty_id, empty_method, empty_name,
                       empty_phone, empty_surname, none_age, none_id,
                       none_method, none_name, none_phone, none_surname,
                       without_age, without_id, without_method, without_name,
                       without_phone, without_surname)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "body", [without_id, without_name, without_surname, without_age, without_method]
)
async def test_add_a_new_user_without_parameter(event_loop, body):
    request_body = json.dumps(get_modified_body(body, phone=PHONE))

    async with websockets.connect(URI) as ws:
        await ws.send(request_body)
        repl = await ws.recv()
        response = json.loads(repl)

    check_only_status(response, Status.FAILURE)


@pytest.mark.asyncio
@pytest.mark.xfail(reason="Поле id не может быть пустым!")
@pytest.mark.parametrize(
    "body", [empty_id, empty_name, empty_surname, empty_age, empty_method]
)
async def test_add_a_new_user_with_empty_parameter(event_loop, body):
    request_body = json.dumps(get_modified_body(body, phone=PHONE))

    async with websockets.connect(URI) as ws:
        await ws.send(request_body)
        repl = await ws.recv()
        response = json.loads(repl)

    check_only_status(response, Status.FAILURE)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "body", [none_id, none_name, none_method, none_age, none_surname]
)
async def test_add_a_new_user_with_none_parameter(event_loop, body):
    request_body = json.dumps(get_modified_body(body, phone=PHONE))

    async with websockets.connect(URI) as ws:
        await ws.send(request_body)
        repl = await ws.recv()
        response = json.loads(repl)

    check_only_status(response, Status.FAILURE)


@pytest.mark.asyncio
@pytest.mark.xfail(reason="Есть возможность добавить пользователя без поля phone!")
@pytest.mark.parametrize("body", [without_phone, empty_phone, none_phone])
async def test_add_a_new_user_with_phone_manipulations(event_loop, body):
    request_body = json.dumps(get_modified_body(body, id=ID))

    async with websockets.connect(URI) as ws:
        await ws.send(request_body)
        repl = await ws.recv()
        response = json.loads(repl)

    check_only_status(response, Status.FAILURE)


@pytest.mark.asyncio
@pytest.mark.xfail(reason="Id и phone могут содержать специальные символы!")
@pytest.mark.parametrize(
    "body",
    [
        get_modified_body(add_body, id="@!#$().[]", phone=PHONE),
        get_modified_body(add_body, method="@!#$().[]", phone=PHONE),
        get_modified_body(add_body, name="@!#$().[]", phone=PHONE),
        get_modified_body(add_body, surname="@!#$().[]", phone=PHONE),
        get_modified_body(add_body, age="@!#$().[]", phone=PHONE),
        get_modified_body(add_body, phone="@!#$().[]"),
    ],
)
async def test_add_a_new_user_without_invalid_value(event_loop, body):
    request_body = json.dumps(body)

    async with websockets.connect(URI) as ws:
        await ws.send(request_body)
        repl = await ws.recv()
        response = json.loads(repl)

    check_only_status(response, Status.FAILURE)


@pytest.mark.asyncio
@pytest.mark.xfail(reason="Поле id и phone не имеют конечной длины допустимого значения")
@pytest.mark.parametrize(
    "body",
    [
        get_modified_body(add_body, id="a" * 100, phone=PHONE),
        get_modified_body(add_body, name="a" * 100, phone=PHONE),
        get_modified_body(add_body, surname="a" * 100, phone=PHONE),
        get_modified_body(add_body, age="1" * 100, phone=PHONE),
        get_modified_body(add_body, phone="1" * 100),
    ],
)
async def test_add_a_new_user_without_invalid_length_value(event_loop, body):
    request_body = json.dumps(body)

    async with websockets.connect(URI) as ws:
        await ws.send(request_body)
        repl = await ws.recv()
        response = json.loads(repl)

    check_only_status(response, Status.FAILURE)


@pytest.mark.asyncio
async def test_add_user_with_same_id(event_loop):
    new_id = ID
    request_body = json.dumps(get_modified_body(add_body, id=new_id, phone=PHONE))

    async with websockets.connect(URI) as ws:
        await ws.send(request_body)
        repl = await ws.recv()
        response1 = json.loads(repl)

    check_only_status(response1, Status.SUCCESS)

    request_body = json.dumps(get_modified_body(add_body, id=new_id, phone=PHONE))

    async with websockets.connect(URI) as ws:
        await ws.send(request_body)
        repl = await ws.recv()
        response2 = json.loads(repl)

    check_only_status(response2, Status.FAILURE)


@pytest.mark.asyncio
async def test_add_user_with_same_phone(event_loop):
    new_phone = PHONE
    request_body = json.dumps(get_modified_body(add_body, id=ID, phone=new_phone))

    async with websockets.connect(URI) as ws:
        await ws.send(request_body)
        repl = await ws.recv()
        response1 = json.loads(repl)

    check_only_status(response1, Status.SUCCESS)

    request_body = json.dumps(get_modified_body(add_body, id=ID, phone=new_phone))

    async with websockets.connect(URI) as ws:
        await ws.send(request_body)
        repl = await ws.recv()
        response2 = json.loads(repl)

    check_only_status(response2, Status.FAILURE)
