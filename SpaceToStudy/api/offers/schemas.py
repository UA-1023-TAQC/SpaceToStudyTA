
unauthorized_schema = {
    "type": "object",
    "properties": {
        "code": {
            "type": "string"
        },
        "message": {
            "type": "string"
        },
        "status": {
            "type": "integer"
        }
    },
    "required": ["code", "message"],
}