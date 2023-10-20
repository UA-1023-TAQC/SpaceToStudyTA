SCHEMA_FOR_ERRORS = {
    "type": "object",
    "properties": {
        "status": {
            "type": "integer"
        },
        "code": {
            "type": "string"
        },
        "message": {
            "type": "string"
        }
    },
    "required": ["status", "code", "message"],
}
