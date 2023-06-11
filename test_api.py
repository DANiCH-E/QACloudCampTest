import requests
import pytest
from functions import *

# API URL
ENDPOINT = "https://jsonplaceholder.typicode.com/posts"

# GET /posts
def test_get_posts():
    # Получаем список всех постов
    response = get_posts(ENDPOINT)
    assert response.status_code == 200
    json_response = response.json()
    print(json_response)

def test_get_post_by_id():
    # Выводим пост с айди 99
    list_posts_response = get_post_by_id(99, ENDPOINT)
    assert list_posts_response.status_code == 200
    data = list_posts_response.json()
    print(data)

def test_get_post_with_wrong_id():
    # Попытка вывода поста с несуществующим айди (Ожидаемый статус код 404)
    list_posts_response = get_post_by_id(300, ENDPOINT)
    assert list_posts_response.status_code == 404

def test_get_posts_by_non_exist_link():
    # Попытка получения постов по несуществующей ссылке
    response = get_posts(ENDPOINT + "/message")
    assert response.status_code == 404


# POST /posts
def test_create_post():
    # Создаем новый пост, загружая в него данные из payload
    payload = new_post_payload()
    create_post_response = create_post(payload, ENDPOINT)
    assert create_post_response.status_code == 201
    data = create_post_response.json()
    print(data)

    # Проверка существования добавленного поста
    # (возникает ошибка, так как он на самом деле не добавляется в БД)
    # но с любым другим айдишником существующего поста работает
    # post_id = data['id']
    # print(post_id)
    # get_post_response = requests.get(ENDPOINT + f"/{post_id}")
    # assert get_post_response.status_code == 200
    # get_post_data = get_post_response.json()
    # print(get_post_data)

def test_create_post_with_custom_id():
    # Попытка создать пост, указывая айди поста вручную(айди генерируется
    # автоматически => значение не будет равно введенному)
    payload = wrong_payload()
    custom_id = payload['id']
    create_post_response = create_post(payload, ENDPOINT)
    data = create_post_response.json()
    true_id = data['id']
    assert true_id != custom_id
    print(data)


# DELETE /posts
def test_delete_post():
    # Создаем новый пост
    payload = new_post_payload()
    create_post_response = create_post(payload, ENDPOINT)
    assert create_post_response.status_code == 201
    data = create_post_response.json()
    post_id = data['id']

    # Удаляем его
    delete_post_response = delete_post(post_id, ENDPOINT)
    assert delete_post_response.status_code == 200

    # Проверяем его отсутствие в списке постов
    get_post_response = get_post_by_id(post_id, ENDPOINT)
    assert get_post_response.status_code == 404

def test_delete_post_with_non_exist_id():
    # Попытка удалить пост с несуществующим айди
    # и это почему то работает...
    # (возможно это как-то автоматически обрабатывается в API)
    delete_post_response = delete_post(9000, ENDPOINT)
    assert delete_post_response.status_code == 200


