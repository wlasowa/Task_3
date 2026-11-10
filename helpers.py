import random
import string


def generate_random_string(length=10):
    letters = string.ascii_lowercase + string.digits
    return "".join(random.choice(letters) for i in range(length))


def generate_user_data():
    return {
        "email": f"{generate_random_string()}@test.ru",
        "password": generate_random_string(),
        "name": generate_random_string(),
    }


def normalize_order_number(number):
    digits = "".join(ch for ch in str(number) if ch.isdigit())
    return digits.zfill(6)
