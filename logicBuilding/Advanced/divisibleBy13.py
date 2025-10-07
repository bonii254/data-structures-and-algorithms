def divisibleBy13(num):
    """
    Number divisble by 13 only if alternating sum of its 3 digits blocks
    taken from right to left is divisible by 13
    """
    num = abs(num)
    if num == 0:
        return True

    s = str(num)
    # Split into 3-digit blocks from right to left
    blocks = [int(s[max(i-3, 0):i]) for i in range(len(s), 0, -3)][::-1]

    alt_sum = 0
    sign = 1
    for block in reversed(blocks):
        alt_sum += sign * block
        sign *= -1  # alternate + and -

    return alt_sum % 13 == 0
           
           
print(divisibleBy13(1234567899))