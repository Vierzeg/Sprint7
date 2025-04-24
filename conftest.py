# conftest.py

import pytest
import allure
import requests
from utils.data_generator import generate_random_courier_data, generate_random_order_data
from helpers.helpers import *

@allure.feature("Создание курьера")
@pytest.fixture
def courier_data():
    """Создаёт нового курьера, возвращает его данные"""
    data = generate_random_courier_data()
    response = requests.post(f"{BASE_URL}/api/v1/courier", json=data)
    assert response.status_code == 201
    yield data

    # Удаление курьера после теста
    login_resp = requests.post(f"{BASE_URL}/api/v1/courier/login", json={
        "login": data["login"],
        "password": data["password"]
    })
    courier_id = login_resp.json().get("id")
    if courier_id:
        requests.delete(f"{BASE_URL}/api/v1/courier/{courier_id}")


@allure.feature("Авторизация курьера")
@pytest.fixture
def courier_id(courier_data):
    """Логинится под курьером и возвращает его id"""
    response = requests.post(f"{BASE_URL}/api/v1/courier/login", json={
        "login": courier_data["login"],
        "password": courier_data["password"]
    })
    assert response.status_code == 200
    return response.json()["id"]

@allure.feature("Создание заказа")
@pytest.fixture
def new_order():
    """Создаёт новый заказ с случайными данными и возвращает его track"""
    order_data = generate_random_order_data()  # Генерация случайных данных для заказа
    response = requests.post(f"{BASE_URL}/api/v1/orders", json=order_data)
    assert response.status_code == 201
    track = response.json().get("track")
    yield track  # Возвращаем track для использования в тестах

    # Удаление заказа после теста
    if track:
        delete_response = requests.delete(f"{BASE_URL}/api/v1/orders/{track}")
        if delete_response.status_code != 200:
            print(f"Не удалось удалить заказ с track: {track}")
