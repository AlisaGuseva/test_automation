import json
import jsonschema
import pytest

result_file = 'result.json'


@pytest.fixture(scope='module')
def user_schema():
    return {
        "type": "object",
        "properties": {
                "name": {"type": "string"},
                "gender": {"type": "string"},
                "address": {"type": "string"},
                "age": {"type": "integer"},
                "books": {
                    "type": "array",
                    "minItems": 1,
                    "uniqueItems": True,
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {"type": "string"},
                            "author": {"type": "string"},
                            "pages": {"type": "integer"},
                            "genre": {"type": "string"}
                        },
                        "required": ["title", "author", "pages", "genre"]
                    }
                }
        },
        "required": ["name", "gender", "address", "age", "books"]
    }


def users():
    with open(result_file, mode='r') as f:
        for user in json.load(f):

            yield user


@pytest.mark.parametrize("user", [u for u in users()])
def test_every_user_entry_schema(user, user_schema):
    '''
    тест проверяет каждую запись о пользователе
    в файле results.json на соответствие схеме
    '''
    try:
        jsonschema.validate(instance=user, schema=user_schema)
    except jsonschema.exceptions.ValidationError as err:
        raise AssertionError