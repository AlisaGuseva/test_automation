import requests


class CommonMethods:
    def __init__(self, url):
        self.url = url

    def custom_request(self):
        return requests.get(f"{self.url}")

    def custom_requests(self, params: str):
        return requests.get(f"{self.url}{params}")

    def custom_post(self, body, headers):
        return requests.post(self.url, body, headers)

    def custom_put(self, body):
        return requests.put(self.url, body)

    def custom_patch(self, body):
        return requests.patch(self.url, body)

    def custom_delete(self):
        return requests.delete(self.url)