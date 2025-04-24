# test_create_courier.py

import requests
import allure
from utils.data_generator import generate_random_courier_data
from helpers.helpers import *

@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.story("Успешное создание курьера")
    @allure.step("Создание нового курьера")
    def test_create_courier_successfully(self):
        data = generate_random_courier_data()
        response = requests.post(f'{BASE_URL}/api/v1/courier', json=data)
        assert response.status_code == 201
        assert response.json().get("ok") is True

    @allure.story("Создание курьера без логина")
    @allure.step("Попытка создать курьера без логина")
    def test_create_courier_without_login(self):
        data = generate_random_courier_data()
        data.pop("login")
        response = requests.post(f'{BASE_URL}/api/v1/courier', json=data)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.story("Создание курьера с дублирующимся логином")
    @allure.step("Попытка создать курьера с логином, который уже существует")
    def test_create_courier_with_duplicate_login(self):
        data = generate_random_courier_data()
        requests.post(f'{BASE_URL}/api/v1/courier', json=data)
        response = requests.post(f'{BASE_URL}/api/v1/courier', json=data)
        assert response.status_code == 409
        assert "Этот логин уже используется" in response.json()["message"]

