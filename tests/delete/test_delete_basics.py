import websockets
import pytest
import json
from utils.constants import URI, ID, PHONE
from tests.add.add_data import add_body
from .delete_data import delete_body
from utils.helpers import get_modified_body
from utils.verifications import check_successful_response, check_only_status
from utils.enums import Method, Status


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
