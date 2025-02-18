from time import time
from get_input import get_input
from get_item import get_item
from get_item import get_itemv2
from store import store_item as store, store_itemv2

def search_v1(stack: list, text: str) -> str:
    """
    Method: 'search_v1()' searches a list and returns a string 
    Arguments: requires two positional arguments 'stack' and 'text'
    Dependencies: 'get_input()', 'get_item()'
    Parameters:
    Stack: represents a list [] object to be searched
    Text: represents a global param 'str' prompting the user to enter a query
globaly
    Returns: query 'str'
    """
    count = 0
    found = False
    while not found:
        missing = get_input(text)
        obj = get_item(stack, missing)
        if obj:
            print(f"{obj} found, took {count+1} tries")
            found = True
        else:
            print(f"{missing} not in stack. please try again")
            store_item(stack, missing)
            count +=1

def search_v4(stack: list, text: str) -> str:
    """
    Method: 'search_v4()' searches a list and returns a string match if one exists and appends the query to the stack if it does not.

    Arguments: requires two positional arguments 'stack' and 'text'

    Dependencies: 'get_input()', 'get_item()', 'store_item()'

    Parameters:

    Stack: represents a list [] object to be searched

    Text: represents  a global param 'str' prompting the user to enter a query

    Returns: query 'str' if it exists within the stack else it adds it and prompts the user to try again.
    """
    count = 0
    found = False
    while not found:
        query = get_input(text)
        request_obj = get_item(stack, query)
        if not request_obj:
            store(stack, query)
            print(f"{query} not in stack \n{query} has been added to stack. please try again")
            count +=1
        else:
            print(f"{request_obj} found, took {count+1} tries")
            found = True

def search_v2(stack: list, text: str) -> str:
    """
    Method: 'search_v2()'searches a list and returns a string \
    Dependencies: 'get_input()', 'get_itemv2()'
    Arguments: requires two ositional arguments 'stack' \ and 'text' 
    Parameters:\
    Stack: a list [] object to be searched
    Text: a global param 'str' prompting the user to enter a query
    """
    start = time()
    count = 0
    found = False
    while not found:
        query = get_input(text)
        request = get_itemv2(stack, query)
        if request:
            end = time()
            total_time = end-start
            print(f"{query} found, took {count+1} retries and {round(total_time, 3)}mls")
            found = True
        else:
            store_item(stack, query)
            print(f"{query} not in stack. please try again")
            count +=1

def search_v3(stack: list, text: str) -> str:
    """
    Method: 'search_v2()'searches a list and returns a string \
    Dependencies: 'get_input()', 'get_itemv2()'
    Arguments: requires two positional arguments 'stack' \ and 'text'
    Parameters:\
    Stack: represents a list [] object to be searched
    Text: represents a global param 'str' prompting the user to enter a query
    Returns: query
    """
    start = time()
    count = 0
    found = False
    while not found:
        query = get_input(text)
        request = get_itemv2(stack, query)
        if not request:
            store_item(stack, query)
            print(f"{query} not in stack. please try again")
            count +=1
            end = time()
            # total_time = end-start
            # print(f"{query} found, took {count+1} retries and {round(total_time, 3)}mls")
        else:
            print(f"{query} found, took {count+1} retries")
            found = True


