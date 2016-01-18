"""COUNTING AND GROUPING"""

def item_order(order):
    """Return orders and quantities

    Example:
        >>> item_order("salad salad hamburger")
        'salad:2 hamburger:1 water:0'

    """

    return "salad:{} hamburger:{} water:{}".format(
        order.count("salad"),
        order.count("hamburger"),
        order.count("water"))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
