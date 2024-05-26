#!/usr/bin/python3
'''Module contains class MyList that inherits from list'''


class MyList(list):
    """
    Class inherits the attributes from list

    Args:
        list: The class list
    """

    def print_sorted(self):
        """
        Function prints a list, sorted by ascension
        """
        sort_list = self.copy()
        sort_list.sort()
        print(sort_list)
