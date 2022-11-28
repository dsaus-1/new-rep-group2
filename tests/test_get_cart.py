from hanlders.cart import get_cart
from main import main

import json

expected_result = {'code': 200, 'message': '1. Яблоки. Голден. (1000 руб/кг) добавлено 2 штук\n2. Груши (200 руб/кг) добавлено 15 штук'}

list_ = [
    {
        "name": "Яблоки. Голден.",
        "price": 1000,
        "num": 2,
        "unit": "кг"
      }, {
        "name": "Груши",
        "price": 200,
        "num": 15,
        "unit": "кг"
      }
]


def test_get_cart():
    '''
    Тест стандартного вывода
    '''
    with open('data/cart.json', 'w', encoding='utf-8') as open_file:
        open_file.write(json.dumps(list_))
    assert get_cart({'code': 200, 'data': 6}) == expected_result


def test_get_cart_404():
    '''
    Тест вывода пустого файла
    '''
    f = open('data/cart.json', 'r+', encoding='utf-8')
    f.truncate(0)
    assert get_cart({"code": 200, "data": 6}) == {'code': 404, 'message': 'В корзине нет товаров'}


def test_get_cart_main():
    '''
    Тест совместной работы с основной функцией
    '''
    result = main({"action": 6})
    assert result.get('action') == expected_result.get('action')