import json

import pytest
import websockets

from tests.add.add_data import add_body
from utils.constants import ID, PHONE, URI
from utils.enums import Method, Status
from utils.helpers import get_modified_body
from utils.verifications import check_only_status, check_successful_response

from .select_data import select_body


@pytest.mark.asyncio
@pytest.mark.xfail(
    reason="Select всегда возвращает satus failure, хотя при этом выдает найденного пользователя!"
)
async def test_select_user_success():
    new_id = ID
    new_phone = PHONE
    request_body_1 = json.dumps(
        get_modified_body(
            add_body, id=new_id, name="Bugs", surname="Bunny", phone=new_phone
        )
    )

    async with websockets.connect(URI) as ws:
        await ws.send(request_body_1)
        repl = await ws.recv()
        response = json.loads(repl)

    check_only_status(response, Status.SUCCESS)

    request_body_2 = json.dumps(get_modified_body(select_body, id=new_id, name="Bugs"))

    async with websockets.connect(URI) as ws:
        await ws.send(request_body_2)
        repl = await ws.recv()
        response = json.loads(repl)

    users = [
        {
            "age": select_body["age"],
            "name": "Bugs",
            "phone": new_phone,
            "surname": "Bunny",
        },
    ]
    check_successful_response(
        response, id=new_id, method=Method.SELECT, status=Status.SUCCESS, users=users
    )


@pytest.mark.asyncio
@pytest.mark.xfail(
    reason="Select всегда возвращает satus failure, хотя при этом выдает найденного пользователя!"
)
async def test_select_user_with_name_and_surname_both():
    new_id = ID

    request_body = json.dumps(get_modified_body(select_body, id=new_id))

    async with websockets.connect(URI) as ws:
        await ws.send(request_body)
        repl = await ws.recv()
        response = json.loads(repl)

    users = [
        {
            "age": 100500,
            "name": "Chuck",
            "phone": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
            "surname": "Dorris",
        }
    ]

    check_successful_response(
        response, id=new_id, method=Method.SELECT, status=Status.SUCCESS, users=users
    )
