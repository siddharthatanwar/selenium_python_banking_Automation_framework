def test_dummyjson_direct():
    import requests
    r = requests.get("https://dummyjson.com/products")
    print(r.status_code)
    assert r.status_code == 200
