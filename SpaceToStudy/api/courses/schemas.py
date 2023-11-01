SCHEMA_FOR_ALL_COURSES = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Course Schema",
    "type": "object",
    "properties": {
        "count": {
            "type": "number"
        },
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
                    "description": {
                        "type": "string"
                    },
                    "author": {
                        "type": "string"
                    },
                    "attachments": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "lessons": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
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
                "required": [
                    "_id",
                    "title",
                    "description",
                    "author",
                    "attachments",
                    "lessons",
                    "createdAt",
                    "updatedAt"
                ]
            }
        }
    },
    "required": ["count", "items"]
}
