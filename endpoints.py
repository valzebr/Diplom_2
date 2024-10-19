from urls import BASE_URL
class Endpoints:

    register_api = BASE_URL + "/api/auth/register" #Создание пользователя
    login_api = BASE_URL + "/api/auth/login" #Авторизация пользователя
    user_api = BASE_URL + "/api/auth/user" #Изменение данных пользователя
    orders_api = BASE_URL + "/api/orders" #Создание заказа