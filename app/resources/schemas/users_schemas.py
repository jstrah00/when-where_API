create_user_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "email": "julianstrah2@gmail.com",
            "name": "Julian",
            "last_name": "Strah",
            "password": "Contrasena123"
        }
    ],
    "required": [
        "email",
        "name",
        "last_name",
        "password"
    ],
    "properties": {
        "email": {
            "$id": "#/properties/email",
            "type": "string",
            "title": "The email schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "pattern": "^\S+@\S+\.\S+$",
            "examples": [
                "julianstrah2@gmail.com"
            ]
        },
        "name": {
            "$id": "#/properties/name",
            "type": "string",
            "title": "The name schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "Julian"
            ]
        },
        "last_name": {
            "$id": "#/properties/last_name",
            "type": "string",
            "title": "The last_name schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "Strah"
            ]
        },
        "password": {
            "$id": "#/properties/password",
            "type": "string",
            "title": "The password schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "minLength": 6,
            "examples": [
                "Contrasena123"
            ]
        }
    },
    "additionalProperties": True
}

authenticate_user_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "email": "julianstrah@gmail.com",
            "password": "Micontra123"
        }
    ],
    "required": [
        "email",
        "password"
    ],
    "properties": {
        "email": {
            "$id": "#/properties/email",
            "type": "string",
            "title": "The email schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "julianstrah@gmail.com"
            ]
        },
        "password": {
            "$id": "#/properties/password",
            "type": "string",
            "title": "The password schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "Micontra123"
            ]
        }
    },
    "additionalProperties": True
}
