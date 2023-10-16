
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

all_offers_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "count": {
      "type": "number"
    },
    "offers": {
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
          "authorFirstName": {
            "type": "string"
          },
          "authorLastName": {
            "type": "string"
          },
          "authorAvgRating": {
            "type": "number"
          },
          "author": {
            "type": "object",
            "properties": {
              "_id": {
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
              "FAQ": {},
              "professionalSummary": {
                "type": "string"
              },
              "photo": {
                "type": "string"
              }
            },
            "required": [
              "_id",
              "totalReviews",
              "FAQ",
              "professionalSummary",
              "photo"
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
            "type": "string"
          },
          "chatId": {
            "type": "string"
          },
          "FAQ": {}
        },
        "required": [
          "_id",
          "price",
          "proficiencyLevel",
          "title",
          "description",
          "languages",
          "authorRole",
          "authorFirstName",
          "authorLastName",
          "authorAvgRating",
          "author",
          "subject",
          "category",
          "FAQ"
        ]
      }
    }
  },
  "required": [
    "count",
    "offers"
  ]
}