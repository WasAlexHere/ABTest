import json

import pytest
import websockets

from utils.constants import ID, PHONE, URI
from utils.enums import Method, Status
from utils.helpers import get_modified_body
from utils.verifications import check_only_status, check_successful_response

from .update_data import (
    update_body,
    without_id,
    without_name,
    without_age,
    without_surname,
    without_phone,
    empty_phone,
    empty_age,
    empty_id,
    empty_name,
    empty_surname,
)


@pytest.mark.asyncio
async def test_update_user_not_in_db():
    new_id = ID
    new_phone = PHONE

    request_body = json.dumps(
        get_modified_body(
            update_body,
            id=new_id,
            name="Steve",
            phone=new_phone,
            surname="NotSoNewMan",
            age=21,
        )
    )

    async with websockets.connect(URI) as ws:
        await ws.send(request_body)
        repl = await ws.recv()
        response = json.loads(repl)

    check_successful_response(
        response, id=new_id, method=Method.UPDATE, status=Status.FAILURE
    )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "body", [without_id, without_name, without_age, without_surname, without_phone]
)
async def test_update_user_without_parameter(body):

    async with websockets.connect(URI) as ws:
        await ws.send(json.dumps(body))
        repl = await ws.recv()
        response_2 = json.loads(repl)

    check_only_status(response_2, Status.FAILURE)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "body", [empty_id, empty_name, empty_age, empty_surname, empty_phone]
)
async def test_update_user_empty_parameter(body):

    async with websockets.connect(URI) as ws:
        await ws.send(json.dumps(body))
        repl = await ws.recv()
        response_2 = json.loads(repl)

    check_only_status(response_2, Status.FAILURE)
