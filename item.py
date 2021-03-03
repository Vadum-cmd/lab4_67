"""
Module which only consists of class Item.
"""
class Item:
    def __init__(self, name: str, price: float):
        """
        Creates object of class Item.

        >>> item_one = Item('book', 110)
        >>> item_one.name
        'book'
        >>> item_one.price
        110
        """
        self.name = name
        self.price = price


    def __str__(self) -> str:
        """
        Gives info about certain object using more-like-human language.

        >>> item_one = Item('book', 110)
        >>> print(item_one)
        It is a book and it costs 110 UAH
        """
        return """It is a {0} and it costs {1} UAH""".format(self.name, self.price)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
