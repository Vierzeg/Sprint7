# test_login_courier.py

import requests
import allure
from utils.data_generator import register_new_courier
from helpers.helpers import *

@allure.feature("Авторизация курьера")
class TestLoginCourier:

    @allure.story("Успешный вход курьера")
    @allure.step("Регистрация курьера и успешный вход с правильными данными")
    def test_login_successfully(self):
        courier = register_new_courier()
        response = requests.post(f'{BASE_URL}/api/v1/courier/login', json={
            "login": courier["login"],
            "password": courier["password"]
        })
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.story("Вход с неправильным паролем")
    @allure.step("Попытка входа с неправильным паролем")
    def test_login_with_wrong_password(self):
        courier = register_new_courier()
        response = requests.post(f'{BASE_URL}/api/v1/courier/login', json={
            "login": courier["login"],
            "password": "wrongpassword"
        })
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.story("Отсутствие поля login")
    @allure.step("Попытка входа без поля login")
    def test_login_without_login_field(self):
        courier = register_new_courier()
        response = requests.post(f'{BASE_URL}/api/v1/courier/login', json={
            "password": courier["password"]
        })
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

