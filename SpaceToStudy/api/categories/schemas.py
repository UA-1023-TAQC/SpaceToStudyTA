
SCHEMA_FOR_ALL_CATEGORIES = {
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
                    "name": {
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
                    },
                    "totalOffers": {
                        "type": "object",
                        "properties": {
                            "student": {
                                "type": "integer"
                            },
                            "tutor": {
                                "type": "integer"
                            }
                        },
                        "required": ["student", "tutor"]
                    },
                    "createdAt": {
                        "type": "string"
                    },
                    "updatedAt": {
                        "type": "string"
                    }
                },
                "required": ["_id", "name", "appearance", "totalOffers", "createdAt", "updatedAt"]
            }
        },
        "count": {
            "type": "integer"
        }
    },
    "required": ["items", "count"]
}

SCHEMA_CATEGORIES_BY_ID = {
  "type": "object",
  "properties": {
    "_id": {
      "type": "string",
    },
    "name": {
      "type": "string"
    },
    "appearance": {
      "type": "object",
      "properties": {
        "icon": {
          "type": "string"
        },
        "color": {
          "type": "string",
        }
      },
      "required": ["icon", "color"]
    },
    "totalOffers": {
      "type": "object",
      "properties": {
        "student": {
          "type": "integer"
        },
        "tutor": {
          "type": "integer"
        }
      },
      "required": ["student", "tutor"]
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
  "required": ["_id", "name", "appearance", "totalOffers", "createdAt", "updatedAt"]
}
