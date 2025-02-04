BYTE = 1048576 # 1Mb

def convert_bytes_to_megabytes(bytes:int) -> int:
    return bytes//BYTE

def convert_megabytes_to_bytes(mb:int) -> int:
    return mb*BYTE



# print(convert_bytes_to_megabytes(3145728))
print(convert_megabytes_to_bytes(1000))