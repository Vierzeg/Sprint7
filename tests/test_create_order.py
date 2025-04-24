# test_create_order.py

import requests
import pytest
import allure
from helpers.helpers import *

order_body_template = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha"
}

@pytest.mark.parametrize("colors", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
@allure.feature("Создание заказа")
@allure.story("Создание заказа с различными цветами")
@allure.step("Создание нового заказа с цветами: {colors}")
def test_create_order_with_various_colors(colors):
    body = order_body_template.copy()
    body["color"] = colors
    response = requests.post(f"{BASE_URL}/api/v1/orders", json=body)
    assert response.status_code == 201
    assert "track" in response.json()
