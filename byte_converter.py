def convert_bytes_to_megabytes(bytes:int) -> int:
    return bytes//1048576

def convert_megabytes_to_bytes(mb:int) -> int:
    return mb*1048576



# print(convert_bytes_to_megabytes(3145728))
print(convert_megabytes_to_bytes(2))