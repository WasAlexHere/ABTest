from utils.enums import Method
from utils.helpers import empty_parameter, none_parameter, without

delete_body = {
    "id": "sfda-11231-123-adfb",
    "method": Method.DELETE,
    "phone": "1234567",
}

without_id = without(delete_body, "id")
without_phone = without(delete_body, "phone")

empty_id = empty_parameter(delete_body, "id")
empty_phone = empty_parameter(delete_body, "phone")

none_id = none_parameter(delete_body, "id")
none_phone = none_parameter(delete_body, "phone")
