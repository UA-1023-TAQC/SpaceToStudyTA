ALL_COOPERATIONS_SCHEMA = {
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
                    "offer": {
                        "type": "object",
                        "properties": {
                            "_id": {
                                "type": "string"
                            },
                            "price": {
                                "type": "number"
                            },
                            "title": {
                                "type": "string"
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
                            }
                        },
                        "required": [
                            "_id",
                            "price",
                            "title",
                            "subject",
                            "category"
                        ]
                    },
                    "initiator": {
                        "type": "string"
                    },
                    "initiatorRole": {
                        "type": "string"
                    },
                    "receiver": {
                        "type": "string"
                    },
                    "receiverRole": {
                        "type": "string"
                    },
                    "proficiencyLevel": {
                        "type": "string"
                    },
                    "price": {
                        "type": "number"
                    },
                    "status": {
                        "type": "string"
                    },
                    "needAction": {
                        "type": "string"
                    },
                    "availableQuizzes": {
                        "type": "array",
                        "items": {}
                    },
                    "finishedQuizzes": {
                        "type": "array",
                        "items": {}
                    },
                    "createdAt": {
                        "type": "string"
                    },
                    "updatedAt": {
                        "type": "string"
                    },
                    "user": {
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
                            "role": {
                                "type": "string"
                            },
                            "photo": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "_id",
                            "firstName",
                            "lastName",
                            "role"
                        ]
                    }
                },
                "required": [
                    "_id",
                    "offer",
                    "initiator",
                    "initiatorRole",
                    "receiver",
                    "receiverRole",
                    "proficiencyLevel",
                    "price",
                    "status",
                    "needAction",
                    "availableQuizzes",
                    "finishedQuizzes",
                    "createdAt",
                    "updatedAt",
                    "user"
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
