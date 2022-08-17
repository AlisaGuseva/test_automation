import pytest
import requests

from jsonschema import validate


def check_200(response):
    return response.status_code == 200


main_url = 'https://jsonplaceholder.typicode.com/'

resources = {
    'posts': 100,
    'comments': 500,
    'albums': 100,
    'photos': 5000,
    'todos': 200,
    'users': 10
}

schema_posts = {
    'type': 'array',
    'properties': {
        'userId': {'type': 'number'},
        'id': {'type': 'number'},
        'title': {'type': 'string'},
        'body': {'type': 'string'}
    }
}
schema_photos = {
    'type': 'array',
    'properties': {
        'albumId': {'type': 'number'},
        'id': {'type': 'number'},
        'title': {'type': 'string'},
        'url': {'type': 'string'},
        'thumbnailUrl': {'type': 'string'}
    }
}
schema_comments = {
    'type': 'array',
    'properties': {
        'postId': {'type': 'number'},
        'id': {'type': 'number'},
        'name': {'type': 'string'},
        'email': {'type': 'string'},
        'body': {'type': 'string'}
    }
}
schema_albums = {
    'type': 'array',
    'properties': {
        'userId': {'type': 'number'},
        'id': {'type': 'number'},
        'title': {'type': 'string'}
    }
}
schema_todos = {
    'type': 'array',
    'properties': {
        'userId': {'type': 'number'},
        'id': {'type': 'number'},
        'title': {'type': 'string'},
        'completed': {'type': 'boolean'}
    }
}
schema_users = {
    'type': 'array',
    'properties': {
        'id': {'type': 'number'},
        'name': {'type': 'string'},
        'username': {'type': 'string'},
        'email': {'type': 'string'},
        'address': {
            'type': 'array',
            'properties': {
                'street': {'type': 'string'},
                'suite': {'type': 'string'},
                'city': {'type': 'string'},
                'zipcode': {'type': 'string'},
            }
        }
    }
}


@pytest.mark.parametrize("req, num", [(i, resources[i]) for i in resources])
def test_resources(req, num):
    response = requests.get(f'{main_url}{req}')
    assert check_200(response)
    assert len(response.json()) == num


def test_post():
    message = {'title': 'foo', 'body': 'bar', 'userId': 1}
    post = requests.post(f'{main_url}posts', data=message)
    assert post.status_code == 201
    assert post.json()['id'] == 101


def test_put():
    message = {'id': 1, 'title': 'totl', 'body': 'buddy', 'userId': 123}
    put = requests.put(f'{main_url}posts/1', message)
    assert check_200(put)


@pytest.mark.parametrize('req, schema', [
    ('posts', schema_posts),
    ('comments', schema_comments),
    ('albums', schema_albums),
    ('photos', schema_photos),
    ('todos', schema_todos),
    ('users', schema_users)
])
def test_validate(req, schema):
    response = requests.get(f'{main_url}{req}')
    assert check_200(response)
    validate(response.json(), schema)


def test_delete():
    delete = requests.delete(f'{main_url}users/1')
    assert check_200(delete)

