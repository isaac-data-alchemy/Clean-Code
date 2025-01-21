def data_from_response(response: dict)-> dict:
    """If the response if Ok, return its payload.
    - response: A dict like::
    {
    "status": 200, # <int>
    "timestamp":"...", # ISO format string of the current dateime
    "payload": {...} #dict with returned data}
    
    - Returns a dictionary like::
    {"data": {...}
    
    - Raises: 
    - ValueError if the HTTP status is !=200}"""
    if response['status'] !=200:
        raise ValueError
    
    return {"data": response["payload"]}