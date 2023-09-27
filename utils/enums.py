from enum import Enum


class Method(str, Enum):
    ADD = "add"
    DELETE = "delete"
    SELECT = "select"
    UPDATE = "update"


class Status(str, Enum):
    SUCCESS = "success"
    FAILURE = "failure"
