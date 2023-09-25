from pytest import fail


def check_successful_response(response, **expected):

    if len(response.keys()) == len(expected.keys()):
        for key, value in expected.items():
            assert response[key] == expected[key], response[key]
    else:
        fail("Incorrect number of keys in response")


def check_only_status(response, expected_status):
    assert response["status"] == expected_status, response["status"]
