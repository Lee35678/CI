import requests

def charge(amount):
    r = requests.post("https://api.example.com/pay", json={"amount": amount})
    return r.json()