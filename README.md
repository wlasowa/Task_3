# Task_3

## UI-автотесты для сервиса Stellar Burgers

## Описание проекта:

conftest.py - фикстуры: driver() (запуск браузера через WebdriverFactory), api_client(), test_user() (создание юзера через API), authorized_driver() (залогиненный браузер)
urls.py - адреса страниц и API
helpers.py - генерация данных юзера и нормализация номера заказа
data.py - названия ингредиентов для сборки бургера
api_client.py - клиент API для создания/удаления тестового юзера
webdriver_factory.py - фабрика браузеров (Chrome/Firefox) с параметром --browser
locators/ - локаторы элементов страниц (main, login, order, profile)
pages/base_page.py - базовый класс: wait-хелперы, навигация по шапке, drag-and-drop
pages/main_page.py - методы главной страницы (конструктор, попап ингредиента, каунтер, оформление заказа)
pages/login_page.py - методы страницы входа и восстановления пароля
pages/order_page.py - методы ленты заказов (счётчики, заказы)
pages/profile_page.py - методы личного кабинета
tests/test_login.py - вход в аккаунт (3 способа) и восстановление пароля (3 теста)
tests/test_main.py - конструктор: переходы в шапке, попап ингредиента, каунтер, оформление заказа
tests/test_order.py - лента заказов: счётчики, «В работе», попап заказа, заказ из истории
tests/test_personal_account.py - личный кабинет (переходы, история заказов, выход)

## Запуск

pip install -r requirements.txt

python -m pytest --browser=chrome
python -m pytest --browser=firefox
