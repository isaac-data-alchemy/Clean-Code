def store_item(stack: list, query: str) -> list:
    return stack.append(query)

def store_itemv2(stack: list, query: str) -> list:
    return stack.extend([query])