SCHEMA_FOR_ALL_LESSONS = {
    "type": "object",
    "properties": {
        "count": {
            "type": "integer",
            "minimum": 0
        },
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "category": {"type": "string"},
                    "_id": {"type": "string"},
                    "author": {"type": "string"},
                    "title": {"type": "string"},
                    "description": {"type": "string"},
                    "attachments": {"type": "array"},
                    "createdAt": {"type": "string", "format": "date-time"},
                    "updatedAt": {"type": "string", "format": "date-time"}
                },
                "required": ["_id", "author", "title", "description", "attachments", "createdAt", "updatedAt"]
            }
        }
    },
    "required": ["count", "items"]
}

SCHEMA_FOR_POST_LESSON = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "description": {"type": "string"},
        "content": {"type": "string"},
        "author": {"type": "string"},
        "attachments": {
            "type": "array",
            "items": {"type": "string"}
        },
        "category": {"type": "string"},
        "_id": {"type": "string"},
        "createdAt": {"type": "string", "format": "date-time"},
        "updatedAt": {"type": "string", "format": "date-time"}
    },
    "required": ["title", "description", "content", "author", "attachments", "category", "_id", "createdAt",
                 "updatedAt"]
}

SCHEMA_FOR_LESSON_BY_ID = {
    "type": "object",
    "properties": {
        "_id": {"type": "string"},
        "author": {"type": "string"},
        "title": {"type": "string"},
        "description": {"type": "string"},
        "attachments": {"type": "array"},
        "createdAt": {"type": "string", "format": "date-time"},
        "updatedAt": {"type": "string", "format": "date-time"}
    },
    "required": ["_id", "author", "title", "description", "attachments", "createdAt", "updatedAt"]
}
