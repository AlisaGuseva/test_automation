import pytest

from ex8.scr.brewery.brewery_api import BreweryApi
from lesson_6_DDT.api_schemas import BrewerySchemas as bs
from lesson_6_DDT.helpers import RANDOM_BREWERY_URL, BREWERY_URL, validatejson


class TestBrewery:
    @pytest.mark.parametrize("by_type, status_code, schema", [
        ("micro", 200, bs.light_wave_schema),
        ("nano", 200, bs.light_wave_schema),
        ("regional", 200, bs.light_wave_schema),
        ("1nani", 400, bs.brewery_400_schema)
    ])
    def test_get_brewery_by_type(self, by_type, status_code, schema):
        brewery = BreweryApi(BREWERY_URL + "?by_type=")
        jsondata = brewery.get_brewery_with_params(param=by_type)
        assert brewery.get_brewery_with_params(param=by_type).status_code == status_code
        assert validatejson(jsondata=jsondata.json(), schema=schema)

    @pytest.mark.parametrize("by, value, status_code, schema", [
        ("?per_page=", 50, 200, bs.light_wave_schema),
        ("?by_city=", "san_diego", 200, bs.light_wave_schema),
        ("?by_dist=", "38.8977,77.0365", 200, bs.light_wave_schema),
        ("?by_name=", "cooper", 200, bs.light_wave_schema),
        ("?by_state=", "new_york", 200, bs.light_wave_schema),
        ("?by_postal=", "44107", 200, bs.light_wave_schema)
    ])
    def test_brewery_with_param(self, by, value, status_code, schema):
        brewery = BreweryApi(BREWERY_URL + by)
        jsondata = brewery.get_brewery_with_params(param=value)
        assert jsondata.status_code == status_code
        assert validatejson(jsondata=jsondata.json(), schema=schema)

    def test_get_random_brewery(self):
        brewery = BreweryApi(RANDOM_BREWERY_URL)
        assert brewery.custom_request().status_code == 200
        assert validatejson(jsondata=brewery.custom_request().json(), schema=bs.light_wave_schema)

    def test_get_non_existed_brewery(self):
        brewery = BreweryApi(RANDOM_BREWERY_URL + "1")
        assert brewery.custom_request().status_code == 404
        assert brewery.custom_request().json().get("message") == "Couldn't find Brewery"
        assert validatejson(jsondata=brewery.custom_request().json(), schema=bs.brewery_not_found_schema)

    @pytest.mark.parametrize("desirable_params, brewery_count, status_code", [
        ("?per_page=5", 5, 200),
        ("?per_page=20", 20, 200),
        ("?per_page=50", 50, 200),
        ("?per_page=200", 50, 200)
    ])
    def test_breweries_per_page(self, desirable_params, brewery_count, status_code):
        brewery = BreweryApi(BREWERY_URL)
        exists_brews = brewery.brewery_length(desirable_params)
        assert brewery.get_brewery_with_params(desirable_params).status_code == status_code
        assert exists_brews == brewery_count