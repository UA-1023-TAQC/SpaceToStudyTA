ALL_OFFERS_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Generated schema for Root",
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
                    "price": {
                        "type": "number"
                    },
                    "proficiencyLevel": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "title": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    },
                    "languages": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "authorRole": {
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
                                },
                                "required": [
                                    "student",
                                    "tutor"
                                ]
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
                                },
                                "required": [
                                    "student",
                                    "tutor"
                                ]
                            },
                            "nativeLanguage": {
                                "type": "string"
                            },
                            "photo": {
                                "type": "string"
                            },
                            "professionalSummary": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "_id",
                            "firstName",
                            "lastName",
                            "totalReviews",
                            "averageRating",
                            "nativeLanguage",
                            "photo",
                            "professionalSummary"
                        ]
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
                        },
                        "required": [
                            "_id",
                            "name"
                        ]
                    },
                    "category": {
                        "type": "object",
                        "properties": {
                            "_id": {
                                "type": "string"
                            },
                            "appearance": {
                                "type": "object",
                                "properties": {
                                    "icon": {
                                        "type": "string"
                                    },
                                    "color": {
                                        "type": "string"
                                    }
                                },
                                "required": [
                                    "icon",
                                    "color"
                                ]
                            }
                        },
                        "required": [
                            "_id",
                            "appearance"
                        ]
                    },
                    "status": {
                        "type": "string"
                    },
                    "FAQ": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "question": {
                                    "type": "string"
                                },
                                "answer": {
                                    "type": "string"
                                },
                                "_id": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "question",
                                "answer",
                                "_id"
                            ]
                        }
                    },
                    "createdAt": {
                        "type": "string"
                    },
                    "updatedAt": {
                        "type": "string"
                    },
                },
                "required": [
                    "_id",
                    "price",
                    "proficiencyLevel",
                    "title",
                    "description",
                    "languages",
                    "authorRole",
                    "author",
                    "subject",
                    "category",
                    "status",
                    "FAQ",
                    "createdAt",
                    "updatedAt",
                ]
            }
        },
        "count": {
            "type": "number"
        }
    },
    "required": [
        "items",
        "count"
    ]
}

SCHEMA_OFFERS_ID = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Generated schema for Root",
    "type": "object",
    "properties": {
        "_id": {
            "type": "string"
        },
        "price": {
            "type": "number"
        },
        "proficiencyLevel": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "title": {
            "type": "string"
        },
        "description": {
            "type": "string"
        },
        "languages": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "authorRole": {
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
                    },
                    "required": [
                        "student",
                        "tutor"
                    ]
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
                    },
                    "required": [
                        "student",
                        "tutor"
                    ]
                },
                "photo": {
                    "type": "string"
                },
                "professionalSummary": {
                    "type": "string"
                }
            },
            "required": [
                "_id",
                "firstName",
                "lastName",
                "totalReviews",
                "averageRating",
                "photo",
                "professionalSummary"
            ]
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
            },
            "required": [
                "_id",
                "name"
            ]
        },
        "category": {
            "type": "object",
            "properties": {
                "_id": {
                    "type": "string"
                },
                "appearance": {
                    "type": "object",
                    "properties": {
                        "icon": {
                            "type": "string"
                        },
                        "color": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "icon",
                        "color"
                    ]
                }
            },
            "required": [
                "_id",
                "appearance"
            ]
        },
        "status": {
            "type": "string"
        },
        "FAQ": {
            "type": "array",
            "items": {}
        },
        "createdAt": {
            "type": "string"
        },
        "updatedAt": {
            "type": "string"
        },
        "chatId": {}
    },
    "required": [
        "_id",
        "price",
        "proficiencyLevel",
        "title",
        "description",
        "languages",
        "authorRole",
        "author",
        "subject",
        "category",
        "status",
        "FAQ",
        "createdAt",
        "updatedAt",
        "chatId"
    ]
}

