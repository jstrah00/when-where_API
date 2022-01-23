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
            "password": "MiliTeAmo"
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
            "first_name": "Juli",
            "last_name": "Strah"
        }
    ],
    "required": [
        "first_name",
        "last_name"
    ],
    "properties": {
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
        }
    },
    "additionalProperties": True
} 

update_user_status_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "status": "active"
        }
    ],
    "required": [
        "status"
    ],
    "properties": {
        "status": {
            "$id": "#/properties/status",
            "default": "",
            "description": "An explanation about the purpose of this instance.",
            "enum": [
                "active",
                "inactive"
            ],
            "examples": [
                "active"
            ],
            "title": "The status schema",
            "type": "string"
        }
    },
    "additionalProperties": True
}

change_password_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "code": "mycode1234",
            "password": "mypassword123"
        }
    ],
    "required": [
        "code",
        "password"
    ],
    "properties": {
        "code": {
            "$id": "#/properties/code",
            "type": "string",
            "title": "The code schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "mycode1234"
            ]
        },
        "password": {
            "$id": "#/properties/password",
            "type": "string",
            "title": "The password schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "mypassword123"
            ]
        }
    },
    "additionalProperties": True
}
