# test_create_courier.py

# import requests
# import allure
# from utils.data_generator import generate_random_courier_data
# from helpers.helpers import *
#
# @allure.feature("Создание курьера")
# class TestCreateCourier:
#
#     @allure.story("Успешное создание курьера")
#     @allure.title("Создание нового курьера с валидными данными")
#     def test_create_courier_successfully(self):
#         data = generate_random_courier_data()
#         with allure.step("Отправка запроса на создание нового курьера"):
#             response = requests.post(f'{BASE_URL}/api/v1/courier', json=data)
#         with allure.step("Проверка успешного ответа"):
#             assert response.status_code == 201
#             assert response.json().get("ok") is True
#
#     @allure.story("Создание курьера без логина")
#     @allure.title("Ошибка создания курьера без логина")
#     def test_create_courier_without_login(self):
#         data = generate_random_courier_data()
#         data.pop("login")
#         with allure.step("Отправка запроса на создание курьера без логина"):
#             response = requests.post(f'{BASE_URL}/api/v1/courier', json=data)
#         with allure.step("Проверка ответа об ошибке"):
#             assert response.status_code == 400
#             assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
#
#     @allure.story("Создание курьера с дублирующимся логином")
#     @allure.title("Ошибка создания курьера с уже существующим логином")
#     def test_create_courier_with_duplicate_login(self):
#         data = generate_random_courier_data()
#         with allure.step("Создание курьера для теста на дубликат"):
#             requests.post(f'{BASE_URL}/api/v1/courier', json=data)
#         with allure.step("Повторная попытка создания курьера с тем же логином"):
#             response = requests.post(f'{BASE_URL}/api/v1/courier', json=data)
#         with allure.step("Проверка ошибки о дубликате"):
#             assert response.status_code == 409
#             assert "Этот логин уже используется" in response.json()["message"]
import requests
import allure
from data.courier_data import *
from helpers.helpers import *
from utils.data_generator import generate_random_courier_data

@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.story("Успешное создание курьера")
    @allure.title("Создание нового курьера с валидными данными")
    def test_create_courier_successfully(self):
        data = generate_random_courier_data()
        with allure.step("Отправка запроса на создание нового курьера"):
            response = requests.post(f'{BASE_URL}/api/v1/courier', json=data)
        with allure.step("Проверка успешного ответа"):
            assert response.status_code == 201
            assert response.json().get("ok") is True

    @allure.story("Создание курьера без логина")
    @allure.title("Ошибка создания курьера без логина")
    def test_create_courier_without_login(self):
        data = generate_random_courier_data()
        data.pop("login")
        with allure.step("Отправка запроса на создание курьера без логина"):
            response = requests.post(f'{BASE_URL}/api/v1/courier', json=data)
        with allure.step("Проверка ответа об ошибке"):
            assert response.status_code == 400
            assert response.json()["message"] == COURIER_MESSAGES["missing_login"]

    @allure.story("Создание курьера с дублирующимся логином")
    @allure.title("Ошибка создания курьера с уже существующим логином")
    def test_create_courier_with_duplicate_login(self, created_courier):
        with allure.step("Повторная попытка создать курьера с тем же логином"):
            response = requests.post(f'{BASE_URL}/api/v1/courier', json=created_courier)
        with allure.step("Проверка ошибки о дубликате логина"):
            assert response.status_code == 409
            assert COURIER_MESSAGES["duplicate_login"] in response.json()["message"]

