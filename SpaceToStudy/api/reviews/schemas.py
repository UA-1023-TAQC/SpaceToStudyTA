SCHEMA_FOR_ALL_REVIEWS = {
    "type": "object",
    "properties": {
        "count": {
            "type": "integer"
        },
        "reviews": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "_id": {
                        "type": "string"
                    },
                    "comment": {
                        "type": ["string", "null"]
                    },
                    "rating": {
                        "type": "integer"
                    },
                    "author": {
                        "type": ["object", "null"],
                        "properties": {
                            "_id": {
                                "type": "string"
                            },
                            "firstName": {
                                "type": "string"
                            },
                            "lastName": {
                                "type": "string"
                            },
                            "photo": {
                                "type": "string"
                            }
                        }
                    },
                    "targetUserId": {
                        "type": "string"
                    },
                    "targetUserRole": {
                        "type": "string"
                    },
                    "offer": {
                        "type": ["object", "null"],
                        "properties": {
                            "_id": {
                                "type": "string"
                            },
                            "proficiencyLevel": {
                                "type": "array",
                                "items": {
                                    "type": "string"
                                }
                            },
                            "subject": {
                                "type": "object",
                                "properties": {
                                    "_id": {
                                        "type": "string"
                                    },
                                    "name": {
                                        "type": "string"
                                    }
                                }
                            },
                            "category": {
                                "type": "object",
                                "properties": {
                                    "_id": {
                                        "type": "string"
                                    },
                                    "name": {
                                        "type": "string"
                                    }
                                }
                            }
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
                "required": ["_id", "rating", "targetUserId", "targetUserRole", "createdAt", "updatedAt"]
            }
        }
    },
    "required": ["count", "reviews"]
}

SCHEMA_FOR_REVIEW_BY_ID = {
    "type": "object",
    "properties": {
        "_id": {"type": "string"},
        "comment": {"type": "string"},
        "rating": {"type": "number"},
        "author": {"type": ["string", "null"]},
        "targetUserId": {"type": "string"},
        "targetUserRole": {"type": "string"},
        "offer": {"type": ["string", "null"]},
        "createdAt": {"type": "string", "format": "date-time"},
        "updatedAt": {"type": "string", "format": "date-time"}
    },
    "required": ["_id", "rating", "targetUserId", "targetUserRole", "createdAt", "updatedAt"]
}
