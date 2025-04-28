# test_create_order.py

# import requests
# import pytest
# import allure
# from helpers.helpers import *
#
# order_body_template = {
#     "firstName": "Naruto",
#     "lastName": "Uchiha",
#     "address": "Konoha, 142 apt.",
#     "metroStation": 4,
#     "phone": "+7 800 355 35 35",
#     "rentTime": 5,
#     "deliveryDate": "2020-06-06",
#     "comment": "Saske, come back to Konoha"
# }
#
# @pytest.mark.parametrize("colors", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
# @allure.feature("Создание заказа")
# @allure.story("Создание заказа с разными цветами")
# @allure.title("Создание заказа с цветами: {colors}")
# def test_create_order_with_various_colors(colors):
#     body = order_body_template.copy()
#     body["color"] = colors
#     with allure.step(f"Отправка запроса на создание заказа с цветами {colors}"):
#         response = requests.post(f"{BASE_URL}/api/v1/orders", json=body)
#     with allure.step("Проверка успешного создания заказа"):
#         assert response.status_code == 201
#         assert "track" in response.json()

import requests
import pytest
import allure
from helpers.helpers import *
from data.order_data import *

@pytest.mark.parametrize("colors", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
@allure.feature("Создание заказа")
@allure.story("Создание заказа с разными цветами")
@allure.title("Создание заказа с цветами: {colors}")
def test_create_order_with_various_colors(colors):
    body = ORDER_TEMPLATE.copy()
    body["color"] = colors
    with allure.step(f"Отправка запроса на создание заказа с цветами {colors}"):
        response = requests.post(f"{BASE_URL}/api/v1/orders", json=body)
    with allure.step("Проверка успешного создания заказа"):
        assert response.status_code == 201
        assert "track" in response.json()
