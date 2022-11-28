# -*- coding: utf-8 -*-
import json

import os


def get_product_list(data, dat={}):

    '''функция для получения списка продуктов
    магазина по заданному фильтру цена/категория '''

    path_catalog = os.path.join(os.path.dirname(__file__), 'data/catalog.json')
    ## открыл файл с списком всех продуктов магазина
    with open(path_catalog, encoding='utf-8') as catalog_data:
        products_ = json.load(catalog_data)

    commands = os.path.join(os.path.dirname(__file__), 'data/command.json')

    ## файл - команда с конфигурацией фильтра цена/категория
    with open(commands, encoding='utf-8') as command_data:
        command_ = json.load(command_data)
    ## Блок для тестов - если нет тестов его пропускаем и идекм в элс
    if dat != {}:
        price = dat["filter"]["price"]
        category = dat["filter"]["category"]
    else:
        price = command_["filter"]["price"]
        category = command_["filter"]["category"]

    price_prod = []  # название продукта
    price_kg = []  # цена за килограмм
    coll = []  # колличесиво штук
    count = 0  # счетчик для случая когда в магазине нет продуктов
    ## если нет продуктов
    for i in products_:
        if category == i['name']:
            count += 1
            if count == 0:
                return []
    ## проверка всех конфигураций фильтров
    if price == None and category == None:
        for i in products_:
            for j in range(len(i['products'])):
                price_prod.append(i["products"][j]["name"])
                price_kg.append(i["products"][j]["price"])
                coll.append(i["products"][j]["balance"])
    elif price != None and category == None:
        for k in products_:
            for i in k['products']:
                ## преобразование фильтра цены в список символов
                list_price = (" ".join(price)).split()
                price_ = i['price']
                if ">" in list_price and "=" in list_price:
                    ##удаляю лишние ввсимволы из списка
                    list_price.remove('>')
                    list_price.remove('=')
                    l_p = ''.join(list_price)
                    if price_ >= int(l_p):
                        price_prod.append(i['name'])
                        price_kg.append(i['price'])
                        coll.append(i['balance'])
                elif "<" in list_price and "=" in list_price:
                    list_price.remove('<')
                    list_price.remove('=')
                    l_p = ''.join(list_price)
                    if price_ <= int(l_p):
                        price_prod.append(i['name'])
                        price_kg.append(i['price'])
                        coll.append(i['balance'])
                elif ">" in list_price:
                    list_price.remove('>')
                    l_p = ''.join(list_price)
                    if price_ > int(l_p):
                        price_prod.append(i['name'])
                        price_kg.append(i['price'])
                        coll.append(i['balance'])
                elif "<" in list_price:
                    list_price.remove('<')
                    l_p = ''.join(list_price)
                    if price_ < int(l_p):
                        price_prod.append(i['name'])
                        price_kg.append(i['price'])
                        coll.append(i['balance'])
    elif price == None and category != None:
        for i in products_:
            if category in i["name"]:
                for j in range(len(i['products'])):
                    price_prod.append(i["products"][j]["name"])
                    price_kg.append(i["products"][j]["price"])
                    coll.append(i["products"][j]["balance"])
    else:
        for i in products_:
            if category in i["name"]:
                for j in i['products']:
                    list_price = (" ".join(price)).split()
                    price_ = j['price']
                    if ">" in list_price and "=" in list_price:
                        list_price.remove('>')
                        list_price.remove('=')
                        l_p = ''.join(list_price)
                        if price_ >= int(l_p):
                            price_prod.append(j['name'])
                            price_kg.append(j['price'])
                            coll.append(j['balance'])
                    elif "<" in list_price and "=" in list_price:
                        list_price.remove('<')
                        list_price.remove('=')
                        l_p = ''.join(list_price)
                        if price_ <= int(l_p):
                            price_prod.append(j['name'])
                            price_kg.append(j['price'])
                            coll.append(j['balance'])
                    elif ">" in list_price:
                        list_price.remove('>')
                        l_p = ''.join(list_price)
                        if price_ > int(l_p):
                            price_prod.append(j['name'])
                            price_kg.append(j['price'])
                            coll.append(j['balance'])
                    elif "<" in list_price:
                        list_price.remove('<')
                        l_p = ''.join(list_price)
                        if price_ < int(l_p):
                            price_prod.append(j['name'])
                            price_kg.append(j['price'])
                            coll.append(j['balance'])
    # словарь для записи получившегося списка продуктов
    d = {'code': 200}
    js_format = []
    ## цикл для собирания нужных данных в строку
    for i in range(len(price_prod)):
        js_format.append(f"{i + 1}. {price_prod[i]} ({price_kg[i]} руб/кг) {coll[i]} шт.\n")
    d['data'] = ''.join(js_format)
    return d


def get_single_product(data):
    pass
