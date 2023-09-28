import json

import pytest
import websockets

from utils.constants import URI
from utils.enums import Status
from utils.verifications import check_only_status

from .select_data import (
    without_id,
    without_name,
    without_surname,
    empty_id,
    empty_name,
    empty_surname,
)


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
