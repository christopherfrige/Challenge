from utils.custom_exceptions import IsNotAnOrderException

class Order:
    def __init__(self, id: int, value: float, store: int, motoboy: int):
        self.id = id
        self.value = value
        self.store = store
        self.motoboy = motoboy


class Base:
    def add_order(self, orderObject: Order) -> bool:
        try:
            if isinstance(orderObject, Order):
                self.orders.append(orderObject)
                return True
            raise IsNotAnOrderException            
        except IsNotAnOrderException:
            print("O objeto passado não é da classe Order")
        return False


class Motoboy(Base):
    def __init__(self, id: int, name: str, deliveryFee: float, storeExclusivity: int = None):
        self.id = id
        self.name = name
        self.deliveryFee = deliveryFee
        self.storeExclusivity = storeExclusivity
        self.orders = []

    def get_payments_from_orders(self, storesList):
        totalPayment = 0
        print(f'* {self.name} - {len(self.orders)} pedidos')
        for order in self.orders:
            paymentFromOrder = order.value * storesList[order.store-1].comissionPercentage
            paymentFromOrder += self.deliveryFee
            totalPayment += paymentFromOrder
            print(f'> Pedido N{order.id} - {storesList[order.store-1].name} - R${paymentFromOrder:.2f}')
        print(f'* Ganho total: R${totalPayment:.2f}')
        print('-'*30)

class Store(Base):
    def __init__(self, id: int, name: str, orderFeePercentage: float):
        self.id = id
        self.name = name
        self.comissionPercentage = orderFeePercentage
        self.orders = []

