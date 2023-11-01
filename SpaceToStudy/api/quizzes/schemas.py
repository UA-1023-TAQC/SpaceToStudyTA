ALL_QUIZZES_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "_id": {
                        "type": "string"
                    },
                    "title": {
                        "type": "string"
                    },
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "author": {
                        "type": "string"
                    },
                    "category": {
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
                "required": ["_id", "title", "items", "author", "category", "createdAt", "updatedAt"]
            }
        },
        "count": {
            "type": "integer"
        }
    },
    "required": ["items", "count"]
}


