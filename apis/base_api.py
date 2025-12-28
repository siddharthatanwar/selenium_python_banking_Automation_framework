import requests
import logging
import time

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://reqres.in",
    "Referer": "https://reqres.in/",
    "Connection": "keep-alive"
}


class BaseAPI:
    def __init__(self, base_url):
        self.logger = logging.getLogger("AutomationLogger")
        self.base_url = base_url.rstrip("/")   # safety

    def get(self, endpoint, headers=None, params=None, retries=2):
        all_headers = DEFAULT_HEADERS.copy()
        if headers:
            all_headers.update(headers)

        url = self.base_url + endpoint

         # 🟦 NEW — log outgoing request
        self.logger.info(f"GET {url}")
        if params:
            self.logger.info(f"Query Params → {params}")

        last_response = None

        for attempt in range(retries + 1):
            last_response = requests.get(
                url,
                headers=all_headers,
                params=params,
                timeout=30
            )

            # 🟦 NEW — log status
            self.logger.info(f"Status: {last_response.status_code}")

            # 🟩 OPTIONAL — only log response body when needed
            self.logger.debug(f"Response Body ← {last_response.text}")

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
        
        # 🟦 NEW — log outgoing request + payload
        self.logger.info(f"POST → {url}")
        if payload:
            self.logger.info(f"Payload → {payload}")

        last_response = None

        for attempt in range(retries + 1):
            last_response = requests.post(
                url,
                json=payload,
                headers=all_headers,
                timeout=30
            )

            #   Log status
            self.logger.info(f"Status: {last_response.status_code}")

            # 🟩 OPTIONAL
            self.logger.debug(f"Response Body ← {last_response.text}")

            if last_response.status_code < 500:
                break

            self.logger.warning(
                f"POST retry {attempt+1} due to status {last_response.status_code}"
            )
            time.sleep(2)

        return last_response
