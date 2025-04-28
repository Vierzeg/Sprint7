# conftest.py

# import pytest
# import allure
# import requests
# from utils.data_generator import generate_random_courier_data, generate_random_order_data
# from helpers.helpers import *
#
# @allure.feature("Создание курьера")
# @pytest.fixture
# def courier_data():
#     """Создаёт нового курьера, возвращает его данные"""
#     data = generate_random_courier_data()
#     response = requests.post(f"{BASE_URL}/api/v1/courier", json=data)
#     assert response.status_code == 201
#     yield data
#
#     # Удаление курьера после теста
#     login_resp = requests.post(f"{BASE_URL}/api/v1/courier/login", json={
#         "login": data["login"],
#         "password": data["password"]
#     })
#     courier_id = login_resp.json().get("id")
#     if courier_id:
#         requests.delete(f"{BASE_URL}/api/v1/courier/{courier_id}")
#
#
# @allure.feature("Авторизация курьера")
# @pytest.fixture
# def courier_id(courier_data):
#     """Логинится под курьером и возвращает его id"""
#     response = requests.post(f"{BASE_URL}/api/v1/courier/login", json={
#         "login": courier_data["login"],
#         "password": courier_data["password"]
#     })
#     assert response.status_code == 200
#     return response.json()["id"]
#
# @allure.feature("Создание заказа")
# @pytest.fixture
# def new_order():
#     """Создаёт новый заказ с случайными данными и возвращает его track"""
#     order_data = generate_random_order_data()  # Генерация случайных данных для заказа
#     response = requests.post(f"{BASE_URL}/api/v1/orders", json=order_data)
#     assert response.status_code == 201
#     track = response.json().get("track")
#     yield track  # Возвращаем track для использования в тестах
#
#     # Удаление заказа после теста
#     if track:
#         delete_response = requests.delete(f"{BASE_URL}/api/v1/orders/{track}")
#         if delete_response.status_code != 200:
#             print(f"Не удалось удалить заказ с track: {track}")
#
# @pytest.fixture
# def created_courier():
#     """Фикстура для создания нового курьера"""
#     data = generate_random_courier_data()
#     response = requests.post(f'{BASE_URL}/api/v1/courier', json=data)
#     assert response.status_code == 201
#     yield data

import pytest
import allure
import requests
from utils.data_generator import generate_random_courier_data, generate_random_order_data
from helpers.helpers import *


@allure.feature("Создание курьера")
@pytest.fixture
def courier_data():
    """Создаёт нового курьера и возвращает его данные"""
    with allure.step("Генерация данных курьера"):
        data = generate_random_courier_data()

    with allure.step("Создание нового курьера через API"):
        response = requests.post(f"{BASE_URL}/api/v1/courier", json=data)
        assert response.status_code == 201, f"Ошибка создания курьера: {response.text}"

    yield data

    with allure.step("Удаление созданного курьера"):
        login_resp = requests.post(f"{BASE_URL}/api/v1/courier/login", json={
            "login": data["login"],
            "password": data["password"]
        })
        courier_id = login_resp.json().get("id")
        if courier_id:
            delete_resp = requests.delete(f"{BASE_URL}/api/v1/courier/{courier_id}")
            if delete_resp.status_code != 200:
                print(f"Не удалось удалить курьера id={courier_id}")


@allure.feature("Авторизация курьера")
@pytest.fixture
def courier_id(courier_data):
    """Логинится под курьером и возвращает его ID"""
    with allure.step("Логин под созданным курьером"):
        response = requests.post(f"{BASE_URL}/api/v1/courier/login", json={
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        assert response.status_code == 200, f"Ошибка логина курьера: {response.text}"
        courier_id = response.json().get("id")
        assert courier_id is not None, "ID курьера не найден в ответе"
        return courier_id


@allure.feature("Создание заказа")
@pytest.fixture
def new_order():
    """Создаёт новый заказ и возвращает его трек-номер"""
    with allure.step("Генерация данных заказа"):
        order_data = generate_random_order_data()

    with allure.step("Создание нового заказа через API"):
        response = requests.post(f"{BASE_URL}/api/v1/orders", json=order_data)
        assert response.status_code == 201, f"Ошибка создания заказа: {response.text}"
        track = response.json().get("track")
        assert track is not None, "Track заказа не получен"

    yield track

    with allure.step("Удаление созданного заказа"):
        if track:
            delete_response = requests.delete(f"{BASE_URL}/api/v1/orders/{track}")
            if delete_response.status_code != 200:
                print(f"Не удалось удалить заказ с track={track}")


@allure.feature("Создание курьера")
@pytest.fixture
def created_courier():
    """Создание нового курьера без удаления после теста"""
    with allure.step("Генерация данных курьера"):
        data = generate_random_courier_data()

    with allure.step("Создание нового курьера через API"):
        response = requests.post(f"{BASE_URL}/api/v1/courier", json=data)
        assert response.status_code == 201, f"Ошибка создания курьера: {response.text}"

    yield data
