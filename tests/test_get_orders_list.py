# test_get_orders_list.py

# import requests
# import allure
# from helpers.helpers import *
#
# @allure.feature("Получение списка заказов")
# @allure.story("Получение списка заказов")
# @allure.title("Успешное получение списка заказов")
# def test_get_order_list_returns_orders():
#     with allure.step("Отправка запроса на получение списка заказов"):
#         response = requests.get(f"{BASE_URL}/api/v1/orders")
#     with allure.step("Проверка корректности ответа"):
#         assert response.status_code == 200
#         assert "orders" in response.json()
#         assert isinstance(response.json()["orders"], list)

import requests
import allure
from helpers.helpers import *

@allure.feature("Получение списка заказов")
@allure.story("Получение списка заказов")
@allure.title("Успешное получение списка заказов")
def test_get_order_list_returns_orders():
    with allure.step("Отправка запроса на получение списка заказов"):
        response = requests.get(f"{BASE_URL}/api/v1/orders")
    with allure.step("Проверка корректности ответа"):
        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)
