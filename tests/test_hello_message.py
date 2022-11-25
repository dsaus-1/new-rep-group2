from hanlders import set_hello_message
from main import main

expected_result = {
    "code": 200,
    "data": "Привет, пользователь! Рады тебя приветствовать в магазине. Здесь ты можешь просмотреть товары, купить что-то. Для более подробной информации вызови помощь командой '1'"
}


def test_hello_message_func():
    result = set_hello_message()

    assert result.get('code') == expected_result.get('code')
    assert result.get('data') == expected_result.get('data')


def test_hello_through_main():
    result = main({"action": 0})

    assert result.get('code') == expected_result.get('code')
    assert result.get('data') == expected_result.get('data')
