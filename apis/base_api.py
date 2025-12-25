# import requests
# import logging
# from core.config_reader import ConfigReader

# class BaseAPI:
#     def __init__(self):
#         self.logger = logging.getLogger("AutomationLogger")
#         self.base_url = ConfigReader.get_env("api")["base_url"]

#     def get(self, endpoint, headers=None, params=None):
#         self.logger.info(f"GET {endpoint}")
#         response = requests.get(
#             self.base_url + endpoint,
#             headers=headers,
#             params=params
#         )
#         return response

#     def post(self, endpoint, payload=None, headers=None):
#         self.logger.info(f"POST {endpoint}")
#         response = requests.post(
#             self.base_url + endpoint,
#             json=payload,
#             headers=headers
#         )
#         return response


# apis/base_api.py

import requests
import logging
import time
from core.config_reader import ConfigReader

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

class BaseAPI:
    def __init__(self):
        self.logger = logging.getLogger("AutomationLogger")
        self.base_url = ConfigReader.get_env("api")["base_url"]

    def get(self, endpoint, headers=None, params=None, retries=2):
        all_headers = DEFAULT_HEADERS.copy()
        if headers:
            all_headers.update(headers)

        url = self.base_url + endpoint
        self.logger.info(f"GET {url}")

        last_response = None
        for attempt in range(retries + 1):
            last_response = requests.get(
                url,
                headers=all_headers,
                params=params,
                timeout=30
            )

            # If NOT server-side issue, break
            if last_response.status_code < 500:
                break

            self.logger.warning(
                f"GET retry {attempt+1} due to status {last_response.status_code}"
            )
            time.sleep(2)

        return last_response

    def post(self, endpoint, payload=None, headers=None, retries=2):
        all_headers = DEFAULT_HEADERS.copy()
        if headers:
            all_headers.update(headers)

        url = self.base_url + endpoint
        self.logger.info(f"POST {url}")

        last_response = None
        for attempt in range(retries + 1):
            last_response = requests.post(
                url,
                json=payload,
                headers=all_headers,
                timeout=30
            )

            if last_response.status_code < 500:
                break

            self.logger.warning(
                f"POST retry {attempt+1} due to status {last_response.status_code}"
            )
            time.sleep(2)

        return last_response
