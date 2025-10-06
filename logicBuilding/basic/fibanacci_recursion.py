def fib0nacci(number):
    if number <= 1:
        return number
    return(fib0nacci(number - 1) + fib0nacci(number - 2))

print(fib0nacci(6))