import websockets
import asyncio
import pytest
import json
from utils.constants import URI


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.mark.asyncio
async def test_add_user_success():
    async with websockets.connect(URI) as ws:
        await ws.send('{"id":"sfda-11231-123-adfb", "method":"add", "name":"Chuck", "surname":"Dorris", "phone":"2128509", "age": 100500}')
        repl = await ws.recv()
        response = json.loads(repl)
        assert response['status'] == 'success'


@pytest.mark.asyncio
async def test_delete_user_success():
    async with websockets.connect(URI) as ws:
        await ws.send('{"method": "delete", "id": "sfda-11231-123-adfb", "phone": "2128509"}')
        repl = await ws.recv()
        response = json.loads(repl)
        assert response['status'] == 'success'

