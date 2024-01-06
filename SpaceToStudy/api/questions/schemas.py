ALL_QUESTIONS_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "_id": {
                            "type": "string"
                        },
                        "title": {
                            "type": "string"
                        },
                        "text": {
                            "type": "string"
                        },
                        "answers": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "text": {
                                            "type": "string"
                                        },
                                        "isCorrect": {
                                            "type": "boolean"
                                        }
                                    },
                                    "required": [
                                        "text",
                                        "isCorrect"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "text": {
                                            "type": "string"
                                        },
                                        "isCorrect": {
                                            "type": "boolean"
                                        }
                                    },
                                    "required": [
                                        "text",
                                        "isCorrect"
                                    ]
                                }
                            ]
                        },
                        "type": {
                            "type": "string"
                        },
                        "category": {
                            "type": "null"
                        },
                        "author": {
                            "type": "string"
                        },
                        "resourceType": {
                            "type": "string"
                        },
                        "createdAt": {
                            "type": "string"
                        },
                        "updatedAt": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "_id",
                        "title",
                        "text",
                        "answers",
                        "type",
                        "category",
                        "author",
                        "resourceType",
                        "createdAt",
                        "updatedAt"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "_id": {
                            "type": "string"
                        },
                        "title": {
                            "type": "string"
                        },
                        "text": {
                            "type": "string"
                        },
                        "answers": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "text": {
                                            "type": "string"
                                        },
                                        "isCorrect": {
                                            "type": "boolean"
                                        }
                                    },
                                    "required": [
                                        "text",
                                        "isCorrect"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "text": {
                                            "type": "string"
                                        },
                                        "isCorrect": {
                                            "type": "boolean"
                                        }
                                    },
                                    "required": [
                                        "text",
                                        "isCorrect"
                                    ]
                                }
                            ]
                        },
                        "type": {
                            "type": "string"
                        },
                        "category": {
                            "type": "null"
                        },
                        "author": {
                            "type": "string"
                        },
                        "resourceType": {
                            "type": "string"
                        },
                        "createdAt": {
                            "type": "string"
                        },
                        "updatedAt": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "_id",
                        "title",
                        "text",
                        "answers",
                        "type",
                        "category",
                        "author",
                        "resourceType",
                        "createdAt",
                        "updatedAt"
                    ]
                }
            ]
        },
        "count": {
            "type": "integer"
        }
    },
    "required": [
        "items",
        "count"
    ]
}

POST_QUESTIONS_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "title": {
            "type": "string"
        },
        "text": {
            "type": "string"
        },
        "answers": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "text": {
                            "type": "string"
                        },
                        "isCorrect": {
                            "type": "boolean"
                        }
                    },
                    "required": [
                        "text",
                        "isCorrect"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "text": {
                            "type": "string"
                        },
                        "isCorrect": {
                            "type": "boolean"
                        }
                    },
                    "required": [
                        "text",
                        "isCorrect"
                    ]
                }
            ]
        },
        "type": {
            "type": "string"
        },
        "category": {
            "type": "null"
        },
        "author": {
            "type": "string"
        },
        "resourceType": {
            "type": "string"
        },
        "_id": {
            "type": "string"
        },
        "createdAt": {
            "type": "string"
        },
        "updatedAt": {
            "type": "string"
        }
    },
    "required": [
        "title",
        "text",
        "answers",
        "type",
        "category",
        "author",
        "resourceType",
        "_id",
        "createdAt",
        "updatedAt"
    ]
}
