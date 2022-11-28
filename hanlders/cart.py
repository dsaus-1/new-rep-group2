import json

def put_product_to_cart(data):
    pass


def get_cart(data):
    '''
     Функция по выводу корзины
    '''
    with open('data/cart.json', encoding='utf-8') as read_file:
        read_cart = json.load(read_file)
        count = 0
        output = []
        if read_cart == []:
            return {
                "code": 404,
                "message": "В корзине нет товаров"
                }
        for i in read_cart:
            count += 1
            output.append(f"{count}. {i['name']} ({i['price']} руб/кг добавлено {i['num']} штук")
        return {
            "code": 200,
            "message": '\n'.join(output)
        }

