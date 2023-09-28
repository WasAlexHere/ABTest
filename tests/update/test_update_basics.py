import json

import pytest
import websockets

from tests.add.add_data import add_body
from utils.constants import ID, PHONE, URI
from utils.enums import Method, Status
from utils.helpers import get_modified_body
from utils.verifications import check_only_status, check_successful_response

from .update_data import update_body


@pytest.mark.asyncio
async def test_update_user_success():
    new_id = ID
    new_phone = PHONE
    request_body_1 = json.dumps(get_modified_body(add_body, id=new_id, phone=new_phone))

    async with websockets.connect(URI) as ws:
        await ws.send(request_body_1)
        repl = await ws.recv()
        response_1 = json.loads(repl)

    check_only_status(response_1, Status.SUCCESS)

    request_body_2 = json.dumps(
        get_modified_body(
            update_body, id=new_id, name="Steve", phone=new_phone, surname="Newman", age=21
        )
    )

    async with websockets.connect(URI) as ws:
        await ws.send(request_body_2)
        repl = await ws.recv()
        response_2 = json.loads(repl)

    check_successful_response(
        response_2, id=new_id, method=Method.UPDATE, status=Status.SUCCESS
    )
