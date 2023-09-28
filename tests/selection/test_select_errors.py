import json

import pytest
import websockets

from tests.add.add_data import add_body
from utils.constants import ID, PHONE, URI
from utils.enums import Method, Status
from utils.helpers import get_modified_body
from utils.verifications import check_only_status, check_successful_response

from .select_data import (select_body, without_id, without_name, without_surname, empty_id, empty_name, empty_surname)


@pytest.mark.asyncio
@pytest.mark.xfail(
    reason="Select всегда возвращает satus failure, хотя при этом выдает найденного пользователя!"
)
@pytest.mark.parametrize("body", [without_id, without_name, without_surname])
async def test_select_user_without_parameter(body):
    async with websockets.connect(URI) as ws:
        await ws.send(json.dumps(body))
        repl = await ws.recv()
        response = json.loads(repl)

    check_only_status(response, Status.FAILURE)


@pytest.mark.asyncio
@pytest.mark.xfail(
    reason="Select всегда возвращает satus failure, хотя при этом выдает найденного пользователя!"
)
@pytest.mark.parametrize("body", [empty_id, empty_name, empty_surname])
async def test_select_user_empty_parameter(body):
    async with websockets.connect(URI) as ws:
        await ws.send(json.dumps(body))
        repl = await ws.recv()
        response = json.loads(repl)

    check_only_status(response, Status.FAILURE)