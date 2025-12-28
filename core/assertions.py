def assert_key_in_response(response_json, key):
    assert key in response_json, f"Key '{key}' not found in response"
