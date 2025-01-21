from time import time

def search_v1(stack: list) -> str:
    """
    Method: 'search_v1()' searches a list and returns a string 
    Arguments: requires one positional argument 'stack' 
    Dependencies: 'get_input()', 'get_item()'
    Parameters:
    Stack: a list object to be searched
    """
    global text
    count = 0
    found = False
    while not found:
        missing = get_input(text)
        obj = get_item(stack, missing)
        if obj:
            print(f"{obj} found, took {count} tries")
            found = True
        else:
            print(f"{missing} not in stack. please try again")
            count +=1

def search_v2(stack: list) -> str:
    """
    Method: 'search_v2()'searches a list and returns a string \
    Dependencies: 'get_input()', 'get_itemv2()'
    Arguments: requires one positional argument 'stack' \
    Parameters:\
    Stack: a list object to be searched
    """
    start = time()
    global text
    count = 0
    found = False
    while not found:
        missing = get_input(text)
        obj = get_itemv2(stack, missing)
        if obj:
            end = time()
            total_time = end-start
            print(f"{obj} found, took {count} tries and {round(total_time, 3)}mls")
            found = True
        else:
            print(f"{missing} not in stack. please try again")
            count +=1            
    