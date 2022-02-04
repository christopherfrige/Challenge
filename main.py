import sys

from entities.classes import Motoboy, Order, Store
from utils.data_loader import get_objects_dict


def main():
    data = get_objects_dict()
    motoboysList = data['motoboysObjects']
    storesList = data['storesObjects']
    ordersList = data['ordersObjects']

    motoboyOrdersMax = round(len(ordersList) / len(motoboysList))

    allocate_all_motoboys(motoboysList, storesList, ordersList, motoboyOrdersMax)

    # Execução com argumento
    if len(sys.argv) > 1:
        try:
            motoboyArgumentId = int(sys.argv[-1])
        except ValueError:
            print('O argumento passado deve ser um número inteiro.')
            return

        for motoboy in motoboysList:
            if motoboyArgumentId == motoboy.id:
                motoboy.get_payments_from_orders(storesList)
                break
        else:
            print('Não há motoboy com esse ID.')
    # Execução sem argumento
    else:
        [motoboy.get_payments_from_orders(storesList) for motoboy in motoboysList]
    

def allocate_all_motoboys(motoboysList, storesList, ordersList, motoboyOrdersMax):
    allocate_exclusive_motoboys(motoboysList, storesList, motoboyOrdersMax)
    allocate_nonexclusive_motoboys(motoboysList, ordersList, motoboyOrdersMax)

def allocate_exclusive_motoboys(motoboysList: list[Motoboy], storesList: list[Store], motoboyOrdersMax: int):
    exclusiveMotoboys = [motoboy for motoboy in motoboysList if motoboy.storeExclusivity]
    for motoboy in exclusiveMotoboys:
        store = [store for store in storesList if store.id==motoboy.storeExclusivity]
        orders = store[0].orders
        deliver_orders(exclusiveMotoboys, orders, motoboyOrdersMax)
        
def allocate_nonexclusive_motoboys(motoboysList: list[Motoboy], ordersList: list[Order], motoboyOrdersMax: int):
    nonExclusiveMotoboys = [motoboy for motoboy in motoboysList if not motoboy.storeExclusivity]
    deliver_orders(nonExclusiveMotoboys, ordersList, motoboyOrdersMax)

def deliver_orders(motoboysSelectedList: list[Motoboy], orders: list[Order], motoboyOrdersMax: int):
    motoboysListCopy = motoboysSelectedList.copy()
    for order in orders:
        if order.motoboy:
            continue
        if len(motoboysListCopy)>0:
            if len(motoboysListCopy[0].orders) >= motoboyOrdersMax:
                continue
            motoboysListCopy[0].add_order(order)
            order.motoboy = motoboysListCopy[0].id
            motoboysListCopy.pop(0)
        if len(motoboysListCopy) == 0:
            motoboysListCopy = motoboysSelectedList.copy()


if __name__ == "__main__":
    main()
