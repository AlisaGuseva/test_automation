import pytest

from lesson_6_DDT.scr.jsonplaceholder.json_placeholder_api import JsonPlaceHolder
from lesson_6_DDT.helpers import DIRECT_PLAYSHOLDER_URL, validatejson, users, headers, patch_body, put_body
from lesson_6_DDT.api_schemas import JsonPlaceHolderSchemas as js


class TestJsonPlacehodler:

    @pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_single_post_request_by_id(self, post_id):
        target = JsonPlaceHolder(DIRECT_PLAYSHOLDER_URL + "posts/").get_json_with_params(post_id)
        assert target.status_code == 200
        assert target.json().get("id") == post_id
        assert validatejson(jsondata=target.json(), schema=js.single_request_schema)

    @pytest.mark.parametrize("userid", [222, 333, 666, 1, 123, 15])
    def test_creating_a_resource(self, userid):
        target = JsonPlaceHolder(DIRECT_PLAYSHOLDER_URL + "posts/").post_resource(users(userid=userid),
                                                                                  headers=headers)
        assert target.status_code == 201
        assert target.json().get("userId") == str(userid)
        assert validatejson(jsondata=target.json(), schema=js.json_create_new_post_schema)

    def test_update_post(self):
        put_target = JsonPlaceHolder(DIRECT_PLAYSHOLDER_URL + "posts/1")
        put_data = put_target.update_post(put_body)
        assert put_data.status_code == 200
        assert put_data.json().get("title") == put_body["title"]
        assert validatejson(jsondata=put_data.json(), schema=js.json_create_new_post_schema)

    def test_patch_title(self):
        patch_target = JsonPlaceHolder(DIRECT_PLAYSHOLDER_URL + "posts/1")
        patch_data = patch_target.patch_post(patch_body)
        assert patch_data.status_code == 200
        assert patch_data.json().get("title") == patch_body["title"]

    def test_delete_post(self):
        delete_target = JsonPlaceHolder(DIRECT_PLAYSHOLDER_URL + "posts/1")
        delete_data = delete_target.delete_post()
        assert delete_data.status_code == 200
        assert delete_data.json() == {}

