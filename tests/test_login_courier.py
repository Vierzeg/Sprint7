# test_login_courier.py

# import requests
# import allure
# from utils.data_generator import register_new_courier
# from helpers.helpers import *
#
# @allure.feature("Авторизация курьера")
# class TestLoginCourier:
#
#     @allure.story("Успешный вход курьера")
#     @allure.title("Успешная авторизация курьера с правильными данными")
#     def test_login_successfully(self):
#         courier = register_new_courier()
#         with allure.step("Отправка запроса на вход с правильными данными"):
#             response = requests.post(f'{BASE_URL}/api/v1/courier/login', json={
#                 "login": courier["login"],
#                 "password": courier["password"]
#             })
#         with allure.step("Проверка успешного входа"):
#             assert response.status_code == 200
#             assert "id" in response.json()
#
#     @allure.story("Ошибка при неправильном пароле")
#     @allure.title("Ошибка авторизации при неверном пароле")
#     def test_login_with_wrong_password(self):
#         courier = register_new_courier()
#         with allure.step("Отправка запроса на вход с неправильным паролем"):
#             response = requests.post(f'{BASE_URL}/api/v1/courier/login', json={
#                 "login": courier["login"],
#                 "password": "wrongpassword"
#             })
#         with allure.step("Проверка сообщения об ошибке"):
#             assert response.status_code == 404
#             assert response.json()["message"] == "Учетная запись не найдена"
#
#     @allure.story("Ошибка при отсутствии поля login")
#     @allure.title("Ошибка авторизации без поля login")
#     def test_login_without_login_field(self):
#         courier = register_new_courier()
#         with allure.step("Отправка запроса на вход без логина"):
#             response = requests.post(f'{BASE_URL}/api/v1/courier/login', json={
#                 "password": courier["password"]
#             })
#         with allure.step("Проверка сообщения об ошибке"):
#             assert response.status_code == 400
#             assert response.json()["message"] == "Недостаточно данных для входа"

import requests
import allure
from utils.data_generator import register_new_courier
from helpers.helpers import *
from data.courier_data import *

@allure.feature("Авторизация курьера")
class TestLoginCourier:

    @allure.story("Успешный вход курьера")
    @allure.title("Успешная авторизация курьера с правильными данными")
    def test_login_successfully(self):
        courier = register_new_courier()
        with allure.step("Отправка запроса на вход с правильными данными"):
            response = requests.post(f'{BASE_URL}/api/v1/courier/login', json={
                "login": courier["login"],
                "password": courier["password"]
            })
        with allure.step("Проверка успешного входа"):
            assert response.status_code == 200
            assert "id" in response.json()

    @allure.story("Ошибка при неправильном пароле")
    @allure.title("Ошибка авторизации при неверном пароле")
    def test_login_with_wrong_password(self):
        courier = register_new_courier()
        with allure.step("Отправка запроса на вход с неправильным паролем"):
            response = requests.post(f'{BASE_URL}/api/v1/courier/login', json={
                "login": courier["login"],
                "password": "wrongpassword"
            })
        with allure.step("Проверка сообщения об ошибке"):
            assert response.status_code == 404
            assert response.json()["message"] == COURIER_MESSAGES["wrong_credentials"]

    @allure.story("Ошибка при отсутствии поля login")
    @allure.title("Ошибка авторизации без поля login")
    def test_login_without_login_field(self):
        courier = register_new_courier()
        with allure.step("Отправка запроса на вход без логина"):
            response = requests.post(f'{BASE_URL}/api/v1/courier/login', json={
                "password": courier["password"]
            })
        with allure.step("Проверка сообщения об ошибке"):
            assert response.status_code == 400
            assert response.json()["message"] == COURIER_MESSAGES["missing_login_field"]
