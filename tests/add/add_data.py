from utils.enums import Method
from utils.helpers import empty_parameter, none_parameter, without

add_body = {
    "id": "sfda-11231-123-adfb",
    "method": Method.ADD,
    "name": "Chuck",
    "surname": "Dorris",
    "phone": "2128509",
    "age": 100500,
}

without_id = without(add_body, "id")
without_method = without(add_body, "method")
without_name = without(add_body, "name")
without_surname = without(add_body, "surname")
without_phone = without(add_body, "phone")
without_age = without(add_body, "age")

empty_id = empty_parameter(add_body, "id")
empty_method = empty_parameter(add_body, "method")
empty_name = empty_parameter(add_body, "name")
empty_surname = empty_parameter(add_body, "surname")
empty_phone = empty_parameter(add_body, "phone")
empty_age = empty_parameter(add_body, "age")

none_id = none_parameter(add_body, "id")
none_method = none_parameter(add_body, "method")
none_name = none_parameter(add_body, "name")
none_surname = none_parameter(add_body, "surname")
none_phone = none_parameter(add_body, "phone")
none_age = none_parameter(add_body, "age")
