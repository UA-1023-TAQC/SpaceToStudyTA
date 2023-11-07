SCHEMA_FOR_ALL_USERS = {
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "mainSubjects": {
                        "type": "object",
                        "required": ["student", "tutor"],
                        "properties": {
                            "student": {
                                "type": "array",
                                "items": {
                                    "type": ["object", "string"],
                                    "required": ["_id", "name", "category", "totalOffers"],
                                    "properties": {
                                        "_id": {
                                            "type": "string"
                                        },
                                        "name": {
                                            "type": "string"
                                        },
                                        "category": {
                                            "type": "string"
                                        },
                                        "totalOffers": {
                                            "type": "number"
                                        }
                                    }
                                }
                            },
                            "tutor": {
                                "type": "array",
                                "items": {
                                    "type": ["object", "string"],
                                    "required": ["_id", "name", "category", "totalOffers"],
                                    "properties": {
                                        "_id": {
                                            "type": "string"
                                        },
                                        "name": {
                                            "type": "string"
                                        },
                                        "category": {
                                            "type": "string"
                                        },
                                        "totalOffers": {
                                            "type": "number"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "totalReviews": {
                        "type": "object",
                        "required": ["student", "tutor"],
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
                        "required": ["student", "tutor"],
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
                        "required": ["student", "tutor", "admin"],
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
                            "type": "string",
                            "enum": ["student", "tutor"]
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
                    "FAQ": {
                        "type": "object",
                        "required": ["student", "tutor"],
                        "properties": {
                            "student": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "required": ["question", "_id", "answer"],
                                    "properties": {
                                        "question": {
                                            "type": "string"
                                        },
                                        "_id": {
                                            "type": "string"
                                        },
                                        "answer": {
                                            "type": "string"
                                        }
                                    }
                                }
                            },
                            "tutor": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "required": ["question", "_id", "answer"],
                                    "properties": {
                                        "question": {
                                            "type": "string"
                                        },
                                        "_id": {
                                            "type": "string"
                                        },
                                        "answer": {
                                            "type": "string"
                                        }
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
                    },
                    "nativeLanguage": {
                        "type": "string"
                    },
                    "address": {
                        "type": "object",
                        "required": ["country", "city"],
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
                        "type": "array"
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
    "required": ["items", "count"]
}

SCHEMA_FOR_USER = {
    "type": "object",
    "properties": {
        "_id": {
            "type": "string"
        },
        "role": {
            "type": "array",
            "items": {
                "type": "string",
                "enum": ["student", "tutor"]
            }
        },
        "firstName": {
            "type": "string"
        },
        "lastName": {
            "type": "string"
        },
        "email": {
            "type": "string",
            "format": "email"
        },
        "categories": {
            "type": "array",
        },
        "mainSubjects": {
            "type": "object",
            "properties": {
                "student": {
                    "type": "array",
                    "items": {
                        "type": ["object", "string"],
                        "required": ["_id", "name", "category", "totalOffers"],
                        "properties": {
                            "_id": {
                                "type": "string"
                            },
                            "name": {
                                "type": "string"
                            },
                            "category": {
                                "type": "string"
                            },
                            "totalOffers": {
                                "type": "number"
                            }
                        }
                    }
                },
                "tutor": {
                    "type": "array",
                    "items": {
                        "type": ["object", "string"],
                        "required": ["_id", "name", "category", "totalOffers"],
                        "properties": {
                            "_id": {
                                "type": "string"
                            },
                            "name": {
                                "type": "string"
                            },
                            "category": {
                                "type": "string"
                            },
                            "totalOffers": {
                                "type": "number"
                            }
                        }
                    }
                }
            }
        },
        "totalReviews": {
            "type": "object",
            "required": ["student", "tutor"],
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
            "required": ["student", "tutor"],
            "properties": {
                "student": {
                    "type": "number"
                },
                "tutor": {
                    "type": "number"
                }
            }
        },
        "nativeLanguage": {
            "type": "string"
        },
        "address": {
            "type": "object",
            "required": ["country", "city"],
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
        "isEmailConfirmed": {
            "type": "boolean"
        },
        "isFirstLogin": {
            "type": "boolean"
        },
        "lastLogin": {
            "type": ["string", "null"],
            "format": "date-time"
        },
        "status": {
            "type": "object",
            "required": ["student", "tutor", "admin"],
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
        "bookmarkedOffers": {
            "type": "array"
        },
        "FAQ": {
            "type": "object",
            "required": ["student", "tutor"],
            "properties": {
                "student": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["question", "_id", "answer"],
                        "properties": {
                            "question": {
                                "type": "string"
                            },
                            "_id": {
                                "type": "string"
                            },
                            "answer": {
                                "type": "string"
                            }
                        }
                    }
                },
                "tutor": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["question", "_id", "answer"],
                        "properties": {
                            "question": {
                                "type": "string"
                            },
                            "_id": {
                                "type": "string"
                            },
                            "answer": {
                                "type": "string"
                            }
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
    "required": [
        "_id",
        "role",
        "firstName",
        "lastName",
        "email",
        "totalReviews",
        "averageRating",
        "isEmailConfirmed",
        "isFirstLogin",
        "lastLogin",
        "status",
        "bookmarkedOffers",
        "createdAt",
        "updatedAt"
    ]
}

SCHEMA_FOR_REVIEWS_BY_USER_ID = {
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
                        "type": "string"
                    },
                    "rating": {
                        "type": "integer"
                    },
                    "author": {
                        "type": "object",
                        "required": ["_id", "firstName", "lastName"],
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
                        "type": "string",
                        "enum": ["student", "tutor"]
                    },
                    "offer": {
                        "type": "object",
                        "required": ["_id", "proficiencyLevel", "subject", "category"],
                        "properties": {
                            "_id": {
                                "type": "string"
                            },
                            "proficiencyLevel": {
                                "type": "array",
                                "items": {
                                    "type": "string",
                                    "enum": ["Beginner", "Intermediate", "Advanced", "Test Preparation", "Professional",
                                             "Specialized"]
                                }
                            },
                            "subject": {
                                "type": "object",
                                "required": ["_id", "name"],
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
                                "required": ["_id", "name"],
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
                "required": [
                    "_id",
                    "comment",
                    "rating",
                    "author",
                    "targetUserId",
                    "targetUserRole",
                    "offer",
                    "createdAt",
                    "updatedAt"
                ]
            }
        }
    },
    "required": ["count", "reviews"]
}

SCHEMA_FOR_REVIEW_STATISTICS_FOR_USER = {
    "type": "object",
    "properties": {
        "stats": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["rating", "count"],
                "properties": {
                    "rating": {
                        "type": "number"
                    },
                    "count": {
                        "type": "integer"
                    }
                }
            }
        }
    }
}

SCHEMA_FOR_COOPERATIONS_BY_USER_ID = {
    "type": "object",
    "required": ["items", "count"],
    "properties": {
        "items": {
            "type": "array",
            "items": {
                "type": "object",
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
                ],
                "properties": {
                    "_id": {
                        "type": "string"
                    },
                    "offer": {
                        "type": "object",
                        "required": ["_id", "price", "title", "subject", "category"],
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
                                "required": ["_id", "name"],
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
                                "required": ["_id", "appearance"],
                                "properties": {
                                    "_id": {
                                        "type": "string"
                                    },
                                    "appearance": {
                                        "type": "object",
                                        "required": ["icon", "color"],
                                        "properties": {
                                            "icon": {
                                                "type": "string"
                                            },
                                            "color": {
                                                "type": "string"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "initiator": {
                        "type": "string"
                    },
                    "initiatorRole": {
                        "type": "string",
                        "enum": ["student", "tutor"]
                    },
                    "receiver": {
                        "type": "string"
                    },
                    "receiverRole": {
                        "type": "string",
                        "enum": ["student", "tutor"]
                    },
                    "proficiencyLevel": {
                        "type": "string",
                        "enum": ["Beginner", "Intermediate", "Advanced", "Test Preparation", "Professional", "Specialized"]
                    },
                    "price": {
                        "type": "number"
                    },
                    "status": {
                        "type": "string",
                        "enum": ["pending", "active", "declined", "closed"]
                    },
                    "needAction": {
                        "type": "string",
                        "enum": ["student", "tutor"]
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
                        "type": "string",
                        "format": "date-time"
                    },
                    "updatedAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "user": {
                        "type": "object",
                        "required": ["_id", "firstName", "lastName", "role"],
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
                        }
                    }
                }
            }
        },
        "count": {
            "type": "integer"
        }
    }
}

SCHEMA_FOR_OFFERS_BY_USER_ID = {
    "type": "object",
    "required": ["count", "items"],
    "properties": {
        "count": {
            "type": "integer"
        },
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
                            "type": "string",
                            "enum": ["Beginner", "Intermediate", "Advanced", "Test Preparation", "Professional",
                                     "Specialized"]
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
                        "type": "string",
                        "enum": ["student", "tutor"]
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
                                "required": ["student", "tutor"]
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
                                "required": ["student", "tutor"]
                            },
                            "FAQ": {
                                "type": "object",
                                "required": ["student", "tutor"],
                                "properties": {
                                    "student": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "required": ["question", "_id", "answer"],
                                            "properties": {
                                                "question": {
                                                    "type": "string"
                                                },
                                                "_id": {
                                                    "type": "string"
                                                },
                                                "answer": {
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    },
                                    "tutor": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "required": ["question", "_id", "answer"],
                                            "properties": {
                                                "question": {
                                                    "type": "string"
                                                },
                                                "_id": {
                                                    "type": "string"
                                                },
                                                "answer": {
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                            "professionalSummary": {
                                "type": "string"
                            },
                            "photo": {
                                "type": "string"
                            }
                        },
                        "required": ["_id", "firstName", "lastName", "totalReviews", "averageRating"]
                    },
                    "subject": {
                        "type": "object",
                        "required": ["_id", "name"],
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
                                "required": ["icon", "color"]
                            }
                        }
                    },
                    "chatId": {
                        "type": ["string", "null"]
                    },
                    "status": {
                        "type": "string",
                        "enum": ["active", "draft", "closed"]
                    },
                    "FAQ": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": ["_id", "question", "answer"],
                            "properties": {
                                "_id": {
                                    "type": "string"
                                },
                                "question": {
                                    "type": "string"
                                },
                                "answer": {
                                    "type": "string"
                                }
                            }
                        }
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
                ],
            }
        }
    }
}
