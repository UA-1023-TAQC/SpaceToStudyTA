import allure
from jsonschema import validate

from tests.api.api_test_runners import APITestRunnerWithStudent
from tests.utils.value_provider import ValueProvider

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


class TestAPICategories(APITestRunnerWithStudent):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/388")
    def test_find_all_categories(self):
        url = f"{ValueProvider.get_base_api_url()}categories"
        validate(instance=self.get_response_json(url), schema=SCHEMA_FOR_ALL_CATEGORIES)
