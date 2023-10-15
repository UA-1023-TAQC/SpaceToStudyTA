SCHEMA_FOR_ALL_USERS = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "mainSubjects": {
                        "type": "object",
                        "properties": {
                            "student": {
                                "type": "array"
                            },
                            "tutor": {
                                "type": "array"
                            }
                        }
                    },
                    "totalReviews": {
                        "type": "object",
                        "properties": {
                            "student": {
                                "type": "number"
                            },
                            "tutor": {
                                "type": "number"
                            }
                        }
                    },
                    "averageRating": {
                        "type": "object",
                        "properties": {
                            "student": {
                                "type": "number"
                            },
                            "tutor": {
                                "type": "number"
                            }
                        }
                    },
                    "status": {
                        "type": "object",
                        "properties": {
                            "student": {
                                "type": "string",
                                "enum": ["active", "blocked"]
                            },
                            "tutor": {
                                "type": "string",
                                "enum": ["active", "blocked"]
                            },
                            "admin": {
                                "type": "string",
                                "enum": ["active", "blocked"]
                            }
                        }
                    },
                    "_id": {
                        "type": "string"
                    },
                    "role": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "firstName": {
                        "type": "string"
                    },
                    "lastName": {
                        "type": "string"
                    },
                    "email": {
                        "type": "string"
                    },
                    "lastLogin": {
                        "type": ["string", "null"],
                        "format": "date-time"
                    },
                    "createdAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "updatedAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "nativeLanguage": {
                        "type": "string"
                    },
                    "address": {
                        "type": "object",
                        "properties": {
                            "country": {
                                "type": "string"
                            },
                            "city": {
                                "type": "string"
                            }
                        }
                    },
                    "professionalSummary": {
                        "type": "string"
                    },
                    "photo": {
                        "type": "string"
                    },
                    "categories": {
                        "type": "array",
                        "items": {
                            "$ref": "categories/schemas.py#/SCHEMA_FOR_ALL_CATEGORIES"
                        }
                    }
                },
                "required": [
                    "mainSubjects",
                    "totalReviews",
                    "averageRating",
                    "status",
                    "_id",
                    "role",
                    "firstName",
                    "lastName",
                    "email",
                    "createdAt",
                    "updatedAt"
                ]
            }
        },
        "count": {
            "type": "number"
        }
    },
    "required": ["items", "count"],
    "components": {
        "category": {
            "$ref": "categories/schemas.py#/SCHEMA_FOR_ALL_CATEGORIES"
        }
    }
}
