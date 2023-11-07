SCHEMA_FOR_ALL_COMMENTS = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Comment Schema",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "_id": {
                "type": "string"
            },
            "author": {
                "type": "object",
                "properties": {
                    "_id": {
                        "type": "string"
                    },
                    "firstName": {
                        "type": "string"
                    },
                    "lastName": {
                        "type": "string"
                    }
                },
                "required": ["_id", "firstName", "lastName"]
            },
            "text": {
                "type": "string"
            },
            "cooperation": {
                "type": "string"
            },
            "createdAt": {
                "type": "string",
                "format": "date-time"
            },
            "updatedAt": {
                "type": "string",
                "format": "date-time"
            }
        },
        "required": ["_id", "author", "text", "cooperation", "createdAt", "updatedAt"]
    }
}

SCHEMA_FOR_COMMENTS = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Comment Schema",
    "type": "object",
    "properties": {
        "_id": {
            "type": "string"
        },
        "author": {
            "type": "string"
        },
        "authorRole": {
            "type": "string"
        },
        "cooperation": {
            "type": "string"
        },
        "text": {
            "type": "string"
        },
        "createdAt": {
            "type": "string",
            "format": "date-time"
        },
        "updatedAt": {
            "type": "string",
            "format": "date-time"
        }
    },
    "required": ["_id", "author", "authorRole", "cooperation", "text", "createdAt", "updatedAt"]
}
