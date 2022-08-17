import requests
import random
from jsonschema import validate
import jsonschema.exceptions


def random_dog():
    url = "https://dog.ceo/api/breeds/list/all"
    random_dog_list = []
    result = requests.get(url).json().get("message")
    for key in result.keys():
        random_dog_list.append(key)
    return random_dog_list


def validatejson(jsondata, schema):
    try:
        validate(instance=jsondata, schema=schema)
    except jsonschema.exceptions.ValidationError:
        return False
    return True


def users(userid):
    body = {
        "title": 'In json we trust!',
        "body": 'laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor',
        "userId": {userid},
    }
    return body


random_dog = random.choice(random_dog())

RANDOM_DOGS = "https://dog.ceo/api/breeds/image/random/"
RANDOM_DOG_BREED = f"https://dog.ceo/api/breed/{random_dog}/images"

RANDOM_BREWERY_URL = "https://api.openbrewerydb.org/breweries/random"
BREWERY_URL = "https://api.openbrewerydb.org/breweries"

DIRECT_PLAYSHOLDER_URL = "https://jsonplaceholder.typicode.com/"

body = {
    "title": 'In json we trust!',
    "body": 'laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor',
    "userId": 2,
}

put_body = {
    "title": 'In',
    "body": 'laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor',
    "userId": 2,
}

patch_body = {
    "title": "patched_body"
}

headers = {
    'Content-type': 'application/json; charset=UTF-8',
}

