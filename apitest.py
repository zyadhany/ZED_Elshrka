import requests

url = 'http://127.0.0.1:5000/api/gen/accounts'

payload = {
    'info': {
        'email': 'youssef',
        'password': '123',
        'handle': 'youssef'
    },
    'attach': {
        'email': 'Youssef',
    }
}

headers = {'Content-Type': 'application/json'}

response = requests.request('POST', url, json=payload, headers=headers)

print(response.text)