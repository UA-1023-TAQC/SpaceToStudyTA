SCHEMA_FOR_ALL_SUBJECTS = {

  "type": "object",
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
          "name": {
            "type": "string"
          },
          "category": {
            "type": "string"
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
        "required": ["_id", "name", "category", "totalOffers", "createdAt", "updatedAt"]
      }
    }
  },
  "required": ["count", "items"]
}
