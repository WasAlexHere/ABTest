import websockets
import asyncio
import json
import sys


async def do_smth():
    uri = "ws://0.0.0.0:8080"
    async with websockets.connect(uri) as ws:
        await ws.send('{"id":"sfda-11231-123-adfa", "method":"update", "name":"Chuck", "surname":"Dorris", "phone":"2128507", "age": 100500}')
        repl = await ws.recv()
        print(json.loads(repl))

asyncio.get_event_loop().run_until_complete(do_smth())
