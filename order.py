"""
Module that initializes class Order.
"""
from location import Location
from item import Item
from vehicle import Vehicle
from typing import List
from random import randint


class Order:
    def __init__(self, user_name: str, location: Location, items: List[Item], \
vehicle= None, orderId= randint(165488695, 234976475)):
        """
        Creates object of class Order.

        >>> location_one = Location('Lviv', 96)
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(orderId = 123213, user_name = 'Oleg', \
            location = location_one, items = my_items)
        >>> my_order.orderId
        123213
        >>> my_order.user_name
        'Oleg'
        >>> my_order.location.city
        'Lviv'
        >>> print(my_order.items[0])
        It is a book and it costs 110 UAH
        >>> print(my_order.items[1])
        It is a chupachups and it costs 44 UAH
        """
        self.user_name = user_name
        self.location = location
        self.items = items
        self.vehicle = vehicle
        self.orderId = orderId


    def __str__(self) -> str:
        """
        Gives info about certain object using more-like-human language.

        >>> location_one = Location('Lviv', 96)
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(orderId = 123213, user_name = 'Oleg', \
            location = location_one, items = my_items)
        >>> print(my_order)
        Order ID: 123213
        Name: Oleg
        Location: Lviv, 96
        Items: book, chupachups
        """ 
        return """Order ID: {0}
Name: {1}
Location: {2}, {3}
Items: {4}""".format(self.orderId, self.user_name, \
    self.location.city, self.location.postoffice, ", ".join([x.name for x in self.items]))


    def calculateAmount(self) -> float:
        """
        Calculates amount of items in certain order.

        >>> location_one = Location('Lviv', 96)
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(user_name = 'Oleg', \
            location = location_one, items = my_items)
        >>> my_order.calculateAmount()
        154
        """
        result = 0

        for el in self.items:
            result += el.price

        return result


    def assignVehicle(self, vehicle_for_order: Vehicle):
        """
        Assigns vehicle for certain order.

        >>> vehicle_one = Vehicle(1)
        >>> location_one = Location('Lviv', 96)
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(orderId = 123213, user_name = 'Oleg', \
            location = location_one, items = my_items)
        >>> my_order.assignVehicle(vehicle_one)
        >>> vehicle_one.isAvailable
        False
        """
        if self.vehicle == None:
            if vehicle_for_order.isAvailable == True:
                self.vehicle = vehicle_for_order
                vehicle_for_order.isAvailable = False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
