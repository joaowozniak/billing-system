import requests

"""
Utils class with the HTTP get and post methods
"""


class Utils:
    def execute_post_request(url, body, date):
        response = requests.post(
            url,
            data=body,
            headers={"Content-Type": "application/json", "Today": date},
        )
        return response

    def execute_get_request(url, date):
        response = requests.get(
            url,
            headers={"Content-Type": "application/json", "Today": date},
        )
        return response
