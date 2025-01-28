def get_item(stack:list, query:str) -> str:
    """ 
        Method: 'get_item()' Checks for a str in a list and returns a str
        Arguments: requires two positional arguments 'stack' and 'list'
        Parameters:
        Stack:  represents a list [] object
        Item: represents a str '' object
        Description: iterates through the stack matching each object to the 'item'
        Returns:   'item' if 'item' object is found within this list it returns 'item' as a str ''
        """
    if query in stack:
        return query


def get_itemv2(stack:list, query:str) -> str:
    """
        Method: 'get_itemv2()' checks for a str in a list and returns a str
        Arguments: requires two positional arguments 'stack' and 'list'
        Parameters:
        Stack: a represents a list [] object
        Item: represents a str '' object
        Description: iterates through the stack and then through each stack within the stack
            running a '==' check for the 'item' within each 'stack'
        Returns:  if 'item' is found within this list it returns the item as a str
        """
    for object in stack:
        for i in object:
            if query== i:
                return query

    