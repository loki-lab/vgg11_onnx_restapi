import requests


if __name__ == "__main__":
    url = "http://127.0.0.1:5000/inference"

    response = requests.post(url, files={"image": open('img/cat_01.jpg', 'rb')})

    print(response.json())
