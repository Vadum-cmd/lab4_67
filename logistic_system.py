"""
Module that initializes class LogisticSystem.
"""
from order import Order
from vehicle import Vehicle
from location import Location
from item import Item
from typing import List


class LogisticSystem:
    def __init__(self, vehicles: List[Vehicle], orders= list()):
        """
        Creates object of class LogisticSystem.

        >>> vehicles = [Vehicle(1), Vehicle(2)]
        >>> logSystem = LogisticSystem(vehicles)
        >>> logSystem.orders
        []
        """
        self.vehicles = vehicles
        self.orders = orders


    def placeOrder(self, order: Order):
        """
        Places your order.

        >>> vehicles = [Vehicle(1), Vehicle(2)]
        >>> logSystem = LogisticSystem(vehicles)
        >>> my_location = Location('Lviv', 53)
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(user_name = 'Oleg', location = my_location, items = my_items)
        >>> logSystem.placeOrder(my_order)
        """
        spare_cars = 0

        for vehicle in self.vehicles:
            if vehicle.isAvailable == True:
                spare_cars += 1

        if spare_cars > 0:
            self.orders.append(order)
            for car in self.vehicles:
                order.assignVehicle(car)

        if order in self.orders:
            result = None
        elif order not in self.orders:
            result = 'There is no available vehicle to deliver an order.'

        return result


    def trackOrder(self, my_orderId: int) -> str:
        """
        Allows you to track certain order by it's ID.

        >>> vehicles = [Vehicle(1), Vehicle(2)]
        >>> logSystem = LogisticSystem(vehicles)
        >>> my_location = Location('Odessa', 3)
        >>> my_items = [Item('flowers',11), Item('shoes',153), Item('helicopter',0.33)]
        >>> my_order = Order(orderId = 232090870, user_name = 'Andrii', location = my_location, items = my_items)
        >>> logSystem.placeOrder(my_order)
        >>> logSystem.trackOrder(232090870)
        'Your order #232090870 is sent to Odessa. Total price: 164.33 UAH.'
        """
        result = 'No such order.'

        for order in self.orders:
            if order.orderId == my_orderId:
                result = """Your order #{0} is sent to {1}. \
Total price: {2} UAH.""".format(order.orderId, order.location.city, order.calculateAmount())

        return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
