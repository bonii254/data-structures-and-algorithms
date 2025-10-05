def get_digital_root(number):
    """have a space complexity of O(1) and time complexity of O(log n)"""
    while number > 9:
        number = sum(int(d) for d in str(number))
        
    return number

def getDigitalRoot(number):
    """has a time complexity of 0(1) and space complexity of 0(n)"""
    if number == 0:
        return 0
    return 9 if number % 9 == 0 else number % 9



print(get_digital_root(89786767))
print(getDigitalRoot(89786767))