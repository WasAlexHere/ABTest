import json

import pytest
import websockets

from utils.constants import ID, PHONE, URI
from utils.enums import Method, Status
from utils.helpers import get_modified_body
from utils.verifications import check_only_status, check_successful_response

from .delete_data import (delete_body, empty_id, empty_phone, none_id,
                          none_phone, without_id, without_phone)


@pytest.mark.asyncio
async def test_delete_user_invalid_phone():
    new_id = ID

    request_body_2 = json.dumps(
        get_modified_body(delete_body, id=new_id, phone="1234567")
    )

    async with websockets.connect(URI) as ws:
        await ws.send(request_body_2)
        repl = await ws.recv()
        response = json.loads(repl)

    check_successful_response(
        response, id=new_id, method=Method.DELETE, status=Status.FAILURE
    )


@pytest.mark.asyncio
async def test_delete_user_invalid_id():
    new_id = "!"

    request_body_2 = json.dumps(
        get_modified_body(delete_body, id=new_id, phone="1234567")
    )

    async with websockets.connect(URI) as ws:
        await ws.send(request_body_2)
        repl = await ws.recv()
        response = json.loads(repl)

    check_successful_response(
        response, id=new_id, method=Method.DELETE, status=Status.FAILURE
    )


@pytest.mark.asyncio
@pytest.mark.parametrize("body", [without_id, without_phone])
async def test_delete_user_without_parameter(body):
    request_body = json.dumps(body)

    async with websockets.connect(URI) as ws:
        await ws.send(request_body)
        repl = await ws.recv()
        response = json.loads(repl)

    check_only_status(response, Status.FAILURE)


@pytest.mark.asyncio
@pytest.mark.parametrize("body", [empty_id, empty_phone])
async def test_delete_user_empty_parameter(body):
    request_body = json.dumps(body)

    async with websockets.connect(URI) as ws:
        await ws.send(request_body)
        repl = await ws.recv()
        response = json.loads(repl)

    check_only_status(response, Status.FAILURE)


@pytest.mark.asyncio
@pytest.mark.parametrize("body", [none_id, none_phone])
async def test_delete_user_none_value_parameter(body):
    request_body = json.dumps(body)

    async with websockets.connect(URI) as ws:
        await ws.send(request_body)
        repl = await ws.recv()
        response = json.loads(repl)

    check_only_status(response, Status.FAILURE)
