# test_get_orders_list.py

import requests
import allure
from helpers.helpers import *

@allure.feature("Получение списка заказов")
@allure.story("Получение списка заказов")
@allure.step("Запрос списка заказов")
def test_get_order_list_returns_orders():
    response = requests.get(f"{BASE_URL}/api/v1/orders")
    assert response.status_code == 200
    assert "orders" in response.json()
    assert isinstance(response.json()["orders"], list)

