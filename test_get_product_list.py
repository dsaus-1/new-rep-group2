from hanlders.products import get_product_list

def test_get_product_list():
    dat = {
        "action": 2,
        "filter": {
            "price": ">=200",
            "category": "Овощи"
        }
    }

    assert get_product_list('data',dat=dat) == {'code': 200,'data': '1. картошка (300 руб/кг) 5 шт.\n2. горох (780 руб/кг) 8 шт.\n'}


def test_2_get_product_list():
    dat = {
        "action": 2,
        "filter": {
            "price": "<=200",
            "category": "Овощи"
        }
    }
    assert get_product_list('data',dat=dat) == {'code': 200, 'data': '1. баклажан (150 руб/кг) 17 шт.\n'}


def test_3_get_product_list():
    dat = {
        "action": 2,
        "filter": {
            "price": None,
            "category": "Овощи"
        }
    }
    assert get_product_list('data',dat=dat) == {'code': 200,'data': '1. картошка (300 руб/кг) 5 шт.\n2. горох (780 руб/кг) 8 шт.\n3. баклажан (150 руб/кг) 17 шт.\n'}


def test_4_get_product_list():
    dat = {
        "action": 2,
        "filter": {
            "price": None,
            "category": "Фрукты"
        }
    }
    assert get_product_list('data',dat=dat) == {'code': 200, 'data': '1. Яблоки. Голден. (1000 руб/кг) 5 шт.\n2. Груши. Сильвер. (500 руб/кг) 3 шт.\n3. сливы. (50 руб/кг) 4 шт.\n'}


def test_5_get_product_list():
    dat = {
        "action": 2,
        "filter": {
            "price": None,
            "category": None
        }
    }
    assert get_product_list('data',dat=dat) == {'code': 200, 'data': '1. Яблоки. Голден. (1000 руб/кг) 5 шт.\n2. Груши. Сильвер. (500 руб/кг) 3 шт.\n3. сливы. (50 руб/кг) 4 шт.\n4. картошка (300 руб/кг) 5 шт.\n5. горох (780 руб/кг) 8 шт.\n6. баклажан (150 руб/кг) 17 шт.\n'}


def test_6_get_product_list():
    dat = {
        "action": 2,
        "filter": {
            "price": ">150",
            "category": "Овощи"
        }
    }
    assert get_product_list('data',dat=dat) == {'code': 200, 'data': '1. картошка (300 руб/кг) 5 шт.\n2. горох (780 руб/кг) 8 шт.\n'}


def test_7_get_product_list():
    dat = {
        "action": 2,
        "filter": {
            "price": "<150",
            "category": "Фрукты"
        }
    }
    assert get_product_list('data',dat=dat) == {'code': 200, 'data': '1. сливы. (50 руб/кг) 4 шт.\n'}


def test_8_get_product_list():
    dat = {
        "action": 2,
        "filter": {
            "price": "<150",
            "category": None
        }
    }
    assert get_product_list('data',dat=dat) == {'code': 200, 'data': '1. сливы. (50 руб/кг) 4 шт.\n'}


def test_9_get_product_list():
    dat = {
        "action": 2,
        "filter": {
            "price": ">150",
            "category": "Овощи"
        }
    }
    assert get_product_list('data',dat=dat) == {'code': 200, 'data': '1. картошка (300 руб/кг) 5 шт.\n2. горох (780 руб/кг) 8 шт.\n'}



def test_10_get_product_list():
    dat = {
        "action": 2,
        "filter": {
            "price": ">150",
            "category": "Фрукты"
        }
    }
    assert get_product_list('data',dat=dat) == {'code': 200, 'data': '1. Яблоки. Голден. (1000 руб/кг) 5 шт.\n2. Груши. Сильвер. (500 руб/кг) 3 шт.\n'}