add_remove_user_roles_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "role": "role_name"
        }
    ],
    "required": [
        "role"
    ],
    "properties": {
        "role": {
            "$id": "#/properties/role",
            "type": "string",
            "title": "The role schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "role_name"
            ]
        }
    },
    "additionalProperties": True
}
