from collections import List 
def get_item(stack:List[str], query:str) -> str:
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


def get_itemv2(stack:List[str], query:str) -> str:
    """
        Method: 'get_itemv2()' checks for a str in a list and returns a str
        Arguments: requires two positional arguments 'stack' and 'query'
        Parameters:
        Stack: a list [] object representing the database storing the user's requested objects
        query: a str '' object representing the user's requested object
        Description: iterates through the stack and then through each stack within the stack
            running a '==' check for the 'query' within each 'stack'
        Returns:  if 'query' is found within this list it returns the query as a str
        """
    for _ in stack:
        for q in _:
            if query== q:
                return query