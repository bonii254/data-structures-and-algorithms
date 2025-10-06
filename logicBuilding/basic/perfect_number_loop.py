def isperfect(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum == number

for i in range(1000):
    if isperfect(i):
        print(i)