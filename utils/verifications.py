import json
from pytest import fail


def check_successful_response(response, **expected):
    resp = json.loads(response)

    if len(resp.keys()) == len(expected.keys()):
        for key, value in expected.items():
            assert resp[key] == expected[key], resp[key]
    else:
        fail("Incorrect number of keys in response")

