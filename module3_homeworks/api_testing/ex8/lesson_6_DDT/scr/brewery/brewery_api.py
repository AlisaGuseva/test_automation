from lesson_6_DDT.scr.common_methods import CommonMethods


class BreweryApi(CommonMethods):
    def __init__(self, url):
        super().__init__(url)

    def get_brewery_with_params(self, param):
        return self.custom_requests(param)

    def brewery_length(self, param):
        return len(self.get_brewery_with_params(param).json())

