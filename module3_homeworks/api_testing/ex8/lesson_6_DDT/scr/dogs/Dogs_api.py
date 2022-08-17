import requests

from lesson_6_DDT.scr.common_methods import CommonMethods


class DogsApi(CommonMethods):
    def __init__(self, url):
        super().__init__(url)

    def dogs_len(self, count) -> int:
        return len(self.dog_request(count).json().get("message"))

    def dog_request(self, number: int = 1):
        return requests.get(f"{self.url}{number}")

