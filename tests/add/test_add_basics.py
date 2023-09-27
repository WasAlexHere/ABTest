import websockets
import pytest
import json
from utils.constants import URI, ID, PHONE
from utils.helpers import get_modified_body
from utils.verifications import check_successful_response, check_only_status
from utils.enums import Method, Status
from .add_data import add_body


@pytest.mark.asyncio
async def test_add_a_new_user_success():
    new_id = ID
    request_body = json.dumps(get_modified_body(add_body, id=new_id, phone=PHONE))

    async with websockets.connect(URI) as ws:
        await ws.send(request_body)
        repl = await ws.recv()
        response = json.loads(repl)

    check_successful_response(
        response, id=new_id, method=Method.ADD, status=Status.SUCCESS
    )


@pytest.mark.asyncio
async def test_add_same_user_twice():
    new_id = ID
    new_phone = PHONE
    request_body = json.dumps(get_modified_body(add_body, id=new_id, phone=new_phone))

    async with websockets.connect(URI) as ws:
        await ws.send(request_body)
        repl = await ws.recv()
        response1 = json.loads(repl)

    check_only_status(response1, Status.SUCCESS)

    request_body = json.dumps(get_modified_body(add_body, id=new_id, phone=new_phone))

    async with websockets.connect(URI) as ws:
        await ws.send(request_body)
        repl = await ws.recv()
        response2 = json.loads(repl)

    check_only_status(response2, Status.FAILURE)
