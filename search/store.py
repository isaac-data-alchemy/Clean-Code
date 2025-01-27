def store_item(stack: list, obj: str) -> list:
    return stack.append(obj)

def store_itemv2(stack: list, obj: str) -> list:
    return stack.extend([obj])