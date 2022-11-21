# -*- coding: utf-8 -*-

import json
from time import sleep

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
        with open('data/command.json') as command_file:
            file_data = command_file.read()
        try:
            result = main(json.loads(file_data))

            print(result)

            f = open('data/command.json', 'r+')
            f.truncate(0)

            if result == 0:
                break

        except:
            print('Ожидаю команды... ')
            sleep(2)
