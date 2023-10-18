SCHEMA_FOR_ALL_CHATS = {
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "_id": {
        "type": "string"
      },
      "members": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
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
                "lastName"
              ]
            },
            "role": {
              "type": "string"
            }
          },
          "required": [
            "user",
            "role"
          ]
        }
      },
      "createdAt": {
        "type": "string"
      },
      "updatedAt": {
        "type": "string"
      },
      "latestMessage": {
        "type": "object",
        "properties": {
          "_id": {
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
              }
            },
            "required": [
              "_id",
              "firstName",
              "lastName"
            ]
          },
          "authorRole": {
            "type": "string"
          },
          "text": {
            "type": "string"
          },
          "chat": {
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
          "author",
          "authorRole",
          "text",
          "chat",
          "createdAt",
          "updatedAt"
        ]
      }
    },
    "required": [
      "_id",
      "members",
      "createdAt",
      "updatedAt"
    ]
  }
}
