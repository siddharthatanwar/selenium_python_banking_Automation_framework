import requests

def test_dummyjson():
    response = requests.get("https://dummyjson.com/products")
    assert response.status_code == 200
