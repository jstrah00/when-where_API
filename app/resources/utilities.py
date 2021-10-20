from jsonschema import validate,exceptions
from app.resources.exceptions import InvalidRequestException

def validate_json_schema(json_data, schema):
    try:
        validate(json_data,schema)
    except exceptions.ValidationError:
        raise InvalidRequestException("Invalid json data")

