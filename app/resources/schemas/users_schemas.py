create_user_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "email": "julianstrahdd@gmail.com",
            "name": "Julian",
            "last_name": "Strah",
            "password": "MiliTeAmo",
            "roles": [
                "user"
            ]
        }
    ],
    "required": [
        "email",
        "name",
        "last_name",
        "password",
        "roles"
    ],
    "properties": {
        "email": {
            "$id": "#/properties/email",
            "type": "string",
            "title": "The email schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "julianstrahdd@gmail.com"
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
            "examples": [
                "MiliTeAmo"
            ]
        },
        "roles": {
            "$id": "#/properties/roles",
            "type": "array",
            "title": "The roles schema",
            "description": "An explanation about the purpose of this instance.",
            "default": [],
            "examples": [
                [
                    "user"
                ]
            ],
            "additionalItems": True,
            "items": {
                "$id": "#/properties/roles/items",
                "anyOf": [
                    {
                        "$id": "#/properties/roles/items/anyOf/0",
                        "type": "string",
                        "title": "The first anyOf schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "user"
                        ]
                    }
                ]
            }
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

update_user_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "email": "julianstrah@gmail.com",
            "first_name": "Juli",
            "last_name": "Strah",
            "role": "admin"
        }
    ],
    "required": [
        "email",
        "first_name",
        "last_name",
        "role"
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
        "first_name": {
            "$id": "#/properties/first_name",
            "type": "string",
            "title": "The first_name schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "Juli"
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
        "role": {
            "$id": "#/properties/role",
            "type": "string",
            "title": "The role schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "admin"
            ]
        }
    },
    "additionalProperties": True
}
