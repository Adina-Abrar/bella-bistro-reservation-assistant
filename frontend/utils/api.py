import requests

BASE_URL = "http://127.0.0.1:8000"


def check_availability(data):
    response = requests.post(
        f"{BASE_URL}/reservation/check-availability",
        json=data,
    )
    return response.json()


def create_reservation(data):
    response = requests.post(
        f"{BASE_URL}/reservation/create-reservation",
        json=data,
    )
    return response.json()


def find_reservation(data):
    response = requests.post(
        f"{BASE_URL}/reservation/find-reservation",
        json=data,
    )
    return response.json()


def modify_reservation(data):
    response = requests.put(
        f"{BASE_URL}/reservation/modify-reservation",
        json=data,
    )
    return response.json()


def cancel_reservation(data):
    response = requests.put(
        f"{BASE_URL}/reservation/cancel-reservation",
        json=data,
    )
    return response.json()