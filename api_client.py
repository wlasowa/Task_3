import allure
import requests

import urls


class ApiClient:
    @allure.step("Зарегистрировать тестового юзера через API")
    def register(self, user_data):
        return requests.post(urls.API_REGISTER, json=user_data)

    @allure.step("Удалить тестового юзера через API")
    def delete_user(self, token):
        headers = {"Authorization": token}
        return requests.delete(urls.API_USER, headers=headers)
