from utils.enums import Method
from utils.helpers import empty_parameter, none_parameter, without

select_body = {
    "id": "sfda-11231-123-adfb",
    "method": Method.SELECT,
    "name": "Chuck",
    "surname": "Dorris",
}

without_id = without(select_body, "id")
without_name = without(select_body, "name")
without_surname = without(select_body, "surname")

empty_id = empty_parameter(select_body, "id")
empty_name = empty_parameter(select_body, "name")
empty_surname = empty_parameter(select_body, "surname")

none_id = none_parameter(select_body, "id")
none_name = none_parameter(select_body, "name")
none_surname = none_parameter(select_body, "surname")