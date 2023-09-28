import websockets
import pytest
import json
from utils.constants import URI, ID, PHONE
from tests.add.add_data import add_body
from .select_data import select_body
from utils.helpers import get_modified_body
from utils.verifications import check_successful_response, check_only_status
from utils.enums import Method, Status


@pytest.mark.asyncio
@pytest.mark.xfail(reason="Select всегда возвращает satus failure, хотя при этом выдает найденного пользователя!")
async def test_select_user_success():
    new_id = ID
    new_phone = PHONE
    request_body_1 = json.dumps(get_modified_body(add_body, id=new_id, name="Bugs", surname="Bunny", phone=new_phone))

    async with websockets.connect(URI) as ws:
        await ws.send(request_body_1)
        repl = await ws.recv()
        response = json.loads(repl)

    check_only_status(response, Status.SUCCESS)

    request_body_2 = json.dumps(
        get_modified_body(select_body, id=new_id, name="Bugs")
    )

    async with websockets.connect(URI) as ws:
        await ws.send(request_body_2)
        repl = await ws.recv()
        response = json.loads(repl)

    check_successful_response(
        response, id=new_id, method=Method.SELECT, status=Status.SUCCESS
    )
