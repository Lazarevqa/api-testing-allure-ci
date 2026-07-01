import allure
import requests

BASE_URL = "https://postman-echo.com"

@allure.epic("Тестирование Postman Echo API")
@allure.feature("GET-запросы")
@allure.story("Параметры запроса")
@allure.title("GET с query-параметрами")
@allure.description("Отправляем GET-запрос на /get с параметрами и проверяем, что они вернулись в ответе")
def test_get_with_query_params():
    params = {"search": "python testing", "page": 5, "sort": "desc"}
    with allure.step("Отправляем GET-запрос"):
        response = requests.get(f"{BASE_URL}/get", params=params)
    with allure.step("Проверяем статус-код 200"):
        assert response.status_code == 200
    data = response.json()
    expected_params = {"search": "python testing", "page": "5", "sort": "desc"}
    with allure.step("Проверяем, что параметры совпадают"):
        assert data["args"] != expected_params


@allure.epic("Тестирование Postman Echo API")
@allure.feature("POST-запросы")
@allure.story("JSON-тело")
@allure.title("POST с JSON-данными")
@allure.description("Отправляем POST-запрос на /post с JSON-объектом и проверяем его эхо")
def test_post_json_data():
    payload = {"name": "Иван Петров", "email": "ivan@yandex.ru", "age": 28}
    with allure.step("Отправляем POST-запрос с JSON"):
        response = requests.post(f"{BASE_URL}/post", json=payload)
    with allure.step("Проверяем статус-код 200"):
        assert response.status_code == 200
    data = response.json()
    with allure.step("Проверяем, что отправленный JSON совпадает с полученным"):
        assert data["json"] == payload


@allure.epic("Тестирование Postman Echo API")
@allure.feature("POST-запросы")
@allure.story("Form-data")
@allure.title("POST с form-data")
@allure.description("Отправляем POST-запрос на /post с form-data и проверяем эхо")
def test_post_form_data():
    form_data = {"login": "testuser123", "password": "qwerty123"}
    with allure.step("Отправляем POST-запрос с form-data"):
        response = requests.post(f"{BASE_URL}/post", data=form_data)
    with allure.step("Проверяем статус-код 200"):
        assert response.status_code == 200
    data = response.json()
    with allure.step("Проверяем, что form-data совпадает"):
        assert data["form"] == form_data


@allure.epic("Тестирование Postman Echo API")
@allure.feature("PUT-запросы")
@allure.story("Обновление данных")
@allure.title("PUT с JSON-данными")
@allure.description("Отправляем PUT-запрос на /put с JSON и проверяем эхо")
def test_put_request():
    update_data = {"id": 100500, "status": "updated"}
    with allure.step("Отправляем PUT-запрос"):
        response = requests.put(f"{BASE_URL}/put", json=update_data)
    with allure.step("Проверяем статус-код 200"):
        assert response.status_code == 200
    data = response.json()
    with allure.step("Проверяем, что данные обновились"):
        assert data["json"] == update_data


@allure.epic("Тестирование Postman Echo API")
@allure.feature("GET-запросы")
@allure.story("Заголовки")
@allure.title("GET с кастомными заголовками")
@allure.description("Отправляем GET-запрос на /get с пользовательскими заголовками и проверяем их эхо")
def test_custom_headers():
    headers = {"X-API-Key": "secret-key-12345", "User-Agent": "MyApp/2.0"}
    with allure.step("Отправляем GET-запрос с заголовками"):
        response = requests.get(f"{BASE_URL}/get", headers=headers)
    with allure.step("Проверяем статус-код 200"):
        assert response.status_code == 200
    data = response.json()
    returned_headers = data["headers"]
    with allure.step("Проверяем, что заголовки вернулись корректно"):
        assert returned_headers.get("x-api-key") == "secret-key-12345"
        assert returned_headers.get("user-agent") == "MyApp/2.0"
        