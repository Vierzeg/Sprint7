import requests

response = requests.get('https://catfact.ninja/fact')
print(response.text)


def test_status_code():
    response = requests.get('https://qa-mesto.praktikum-services.ru/api/cards',
                        headers={'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NTEyYzhmMzFjNjE2ZTAwM2QwNzJiOGIiLCJpYXQiOjE2OTU3Mjk5MDcsImV4cCI6MTY5NjMzNDcwN30.jl5gD4iuZqH5Dshf9t29rIdYIouOyuCxWXDnUi-kxPo'})

    print(response.status_code)
    assert 200 == response.status_code
