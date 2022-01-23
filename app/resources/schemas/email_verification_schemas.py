verify_email_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "code": "examplecode1234"
        }
    ],
    "required": [
        "code"
    ],
    "properties": {
        "code": {
            "$id": "#/properties/code",
            "type": "string",
            "title": "The code schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "examplecode1234"
            ]
        }
    },
    "additionalProperties": True
}
