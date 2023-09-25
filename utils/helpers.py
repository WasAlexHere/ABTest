def get_modified_body(body: dict, **kwargs) -> dict:
    new = body.copy()
    for key, value in kwargs.items():
        new[key] = value
    return new


def without(body: dict, key: str) -> dict:
    new = body.copy()
    new.pop(key)
    return new


def none_parameter(body: dict, key: str) -> dict:
    new = body.copy()
    new[key] = None
    return new


def empty_parameter(body: dict, key: str) -> dict:
    new = body.copy()
    new[key] = ""
    return new
