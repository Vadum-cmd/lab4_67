"""
Module which only consists of class Vehicle.
"""
class Vehicle:
    def __init__(self, vehicleNo: int, isAvailable= True):
        """
        Creates object of class Vehicle.

        >>> vehicle_one = Vehicle(1)
        >>> vehicle_one.vehicleNo
        1
        >>> vehicle_one.isAvailable
        True
        """
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable


if __name__ == "__main__":
    import doctest
    doctest.testmod()
