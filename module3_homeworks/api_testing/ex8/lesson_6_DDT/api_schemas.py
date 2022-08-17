class DogSchemas:
    schema_dog_request = {
        "type": "object",
        "properties": {
            "message": {"type": ["array", "string"]},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }


class BrewerySchemas:
    light_wave_schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "array",
        "items": [
            {
                "type": "object",
                "properties": {
                    "id": {
                        "type": ["null", "string"]
                    },
                    "name": {
                        "type": ["null", "string"]
                    }
                },
                "required": [
                    "id",
                    "name"
                ]
            }
        ]
    }

    brewery_400_schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "errors": {
                "type": "array",
                "items": [
                    {
                        "type": "string"
                    }
                ]
            }
        },
        "required": [
            "errors"
        ]
    }

    brewery_not_found_schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "message": {
                "type": "string"
            }
        },
        "required": [
            "message"
        ]
    }


class JsonPlaceHolderSchemas:
    single_request_schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "userId": {
                "type": "integer"
            },
            "id": {
                "type": "integer"
            },
            "title": {
                "type": "string"
            },
            "body": {
                "type": "string"
            }
        },
        "required": [
            "userId",
            "id",
            "title",
            "body"
        ]
    }

    json_create_new_post_schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "title": {
                "type": "string"
            },
            "body": {
                "type": "string"
            },
            "userId": {
                "type": "string"
            },
            "id": {
                "type": "integer"
            }
        },
        "required": [
            "title",
            "body",
            "userId",
            "id"
        ]
    }
