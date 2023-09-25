import websockets
import asyncio
import pytest
import json
from utils.constants import URI, ID, add_body, PHONE, delete_body
from utils.helpers import get_modified_body
from utils.verifications import check_successful_response
from utils.enums import Method, Status

new_phone = PHONE
new_id = ID



@pytest.mark.asyncio
async def test_delete_user_success():
    request_body = json.dumps(get_modified_body(delete_body, id=new_id, phone=new_phone))
    async with websockets.connect(URI) as ws:
        await ws.send(request_body)
        repl = await ws.recv()
        response = json.loads(repl)
        assert response['status'] == 'success'
