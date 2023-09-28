import json

import pytest
import websockets

from tests.add.add_data import add_body
from utils.constants import ID, PHONE, URI
from utils.enums import Method, Status
from utils.helpers import get_modified_body
from utils.verifications import check_only_status, check_successful_response

from .delete_data import delete_body


@pytest.mark.asyncio
async def test_delete_user_success():
    new_id = ID
    new_phone = PHONE
    request_body_1 = json.dumps(get_modified_body(add_body, id=new_id, phone=new_phone))

    async with websockets.connect(URI) as ws:
        await ws.send(request_body_1)
        repl = await ws.recv()
        response = json.loads(repl)

    check_only_status(response, Status.SUCCESS)

    request_body_2 = json.dumps(
        get_modified_body(delete_body, id=new_id, phone=new_phone)
    )

    async with websockets.connect(URI) as ws:
        await ws.send(request_body_2)
        repl = await ws.recv()
        response = json.loads(repl)

    check_successful_response(
        response, id=new_id, method=Method.DELETE, status=Status.SUCCESS
    )
