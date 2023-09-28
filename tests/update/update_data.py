from utils.enums import Method
from utils.helpers import without, empty_parameter, none_parameter

update_body = {
    "id": "sfda-11231-123-adfb",
    "method": Method.UPDATE,
    "name": "Chuck",
    "surname": "Dorris",
    "phone": "2128509",
    "age": 100500,
}

without_id = without(update_body, "id")
without_name = without(update_body, "name")
without_surname = without(update_body, "surname")
without_phone = without(update_body, "phone")
without_age = without(update_body, "age")

empty_id = empty_parameter(update_body, "id")
empty_name = empty_parameter(update_body, "name")
empty_surname = empty_parameter(update_body, "surname")
empty_phone = empty_parameter(update_body, "phone")
empty_age = empty_parameter(update_body, "age")

none_id = none_parameter(update_body, "id")
none_name = none_parameter(update_body, "name")
none_surname = none_parameter(update_body, "surname")
none_phone = none_parameter(update_body, "phone")
none_age = none_parameter(update_body, "age")
