import json

import consts
from hanlders import categories, products, set_hello_message, unknown_message, cart


def main(data):
    if data.get('action') == consts.HELLO:
        return set_hello_message()

    elif data.get('action') == consts.LIST_PRODUCTS:
        return products.get_product_list(data)

    elif data.get('action') == consts.SINGLE_PRODUCT:
        return products.get_single_product(data)

    elif data.get('action') == consts.LIST_CATEGORIES:
        return categories.get_category_list(data)

    elif data.get('action') == consts.PUT_TO_THE_CART:
        return cart.put_product_to_cart(data)

    elif data.get('action') == consts.SHOW_CART:
        return cart.get_cart(data)

    elif data.get('action') == consts.EXIT:
        return 0

    else:
        return unknown_message()


if __name__ == '__main__':
    while True:
        # Первый вариант сделать через ввод JSON в файл
        json_data = input('JSON: ')
        result = main(json.loads(json_data))
        print(result)

        # Второй вариант сделать через вписывание данных в файл, тут нужно выбрать, мне кажется, второй вариант будет интереснее
        with open('data/command.json') as command_file:
            result = main(json.load(command_file))

        with open('data/command.json', 'w') as command_file:
            command_file.write('')
        print(result)

        if result == 0:
            break
