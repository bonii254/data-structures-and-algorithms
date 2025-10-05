def toBinary(decimal):
    if decimal == 0:
        return "0"
    if decimal == 1:
        return "1"
    while decimal > 0:
        decimal % 2