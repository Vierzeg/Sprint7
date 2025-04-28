# data_generator.py

import random
import string
import requests
from helpers.helpers import *
# Генерация случайной строки (например, для имени или адреса)
def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Генерация случайных данных для курьера
def generate_random_courier_data():
    return {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string()
    }

# Генерация случайных данных для заказа
def generate_random_order_data():
    return {
        "firstName": generate_random_string(),
        "lastName": generate_random_string(),
        "address": f"{generate_random_string(5)} Street, {random.randint(1, 100)}",
        "metroStation": random.randint(1, 10),
        "phone": f"+7 800 555 35 {random.randint(10, 99)}",
        "rentTime": random.randint(1, 10),
        "deliveryDate": "2025-06-06",  # можно сделать случайным, если необходимо
        "comment": "Random comment",
        "color": random.choice([["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    }

def register_new_courier():
    data = generate_random_courier_data()
    response = requests.post(f'{BASE_URL}/api/v1/courier', json=data)
    if response.status_code == 201:
        return data
    return {}
