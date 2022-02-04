import json

from entities.classes import Motoboy, Order, Store
from utils.global_variables import DATABASE_FILE_PATH


def load_data_from_json(jsonFilePath: str) -> dict:
    with open(jsonFilePath, 'r') as file:
        return json.load(file)

def generate_objects(databaseFullDict: dict, objectKey: str) -> list:
    singleDict = databaseFullDict[objectKey]

    objectsList = []
    if objectKey == "motoboys":
        for item in singleDict:
            objectsList.append(Motoboy(item["id"], item["name"], item["deliveryFee"], item["storeExclusivity"]))
    elif objectKey == "stores":
        for item in singleDict:
            objectsList.append(Store(item["id"], item["name"], item["comissionPercentage"]))
    elif objectKey == "orders":
        for item in singleDict:
            objectsList.append(Order(item["id"], item["value"], item["store"], item["motoboy"]))
    else:
        print('Sem essa chave no dicionário!')
    return objectsList

def assign_orders_to_stores(storesList: list[Store], ordersList: list[Order]) -> list[Store]:
    for order in ordersList:
        storesList[order.store-1].add_order(order)
    return storesList

def get_objects_dict() -> dict[Motoboy, Store, Order]:
    databaseFullDict = load_data_from_json(DATABASE_FILE_PATH)

    motoboysList = generate_objects(databaseFullDict, 'motoboys')
    storesList = generate_objects(databaseFullDict, 'stores')
    ordersList = generate_objects(databaseFullDict, 'orders')

    storesList = assign_orders_to_stores(storesList, ordersList)

    return {
        'motoboysObjects': motoboysList, 
        'storesObjects': storesList, 
        'ordersObjects': ordersList
    }
