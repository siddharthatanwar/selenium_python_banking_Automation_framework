def test_direct_reqres():
    import requests
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/131.0.0.0 Safari/537.36"
        )
    }
    r = requests.get(
        "https://reqres.in/api/users?page=2",
        headers=headers
    )
    print(r.status_code)
    print(r.text)
