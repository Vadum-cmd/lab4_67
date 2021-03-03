"""
Module which only consists of class Location.
"""
class Location:
    def __init__(self, city: str, postoffice: int):
        """
        Creates object of class Location.

        >>> first_location = Location("Lviv", 69)
        >>> first_location.city
        'Lviv'
        >>> first_location.postoffice
        69
        """
        self.city = city
        self.postoffice = postoffice


if __name__ == "__main__":
    import doctest
    doctest.testmod()
