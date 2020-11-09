def factorial(n):
    '''Silnia iteracyjnie.'''
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fibonacci(n):
    '''N-ty element ciagu fibonacciego iteracyjnie.'''
    result = 0
    if n == 0:
        return 0
    elif n == 2:
        return 1
    else:
        a = 0
        b = 1
    for i in range(2, n):
        result = a + b
        a = b
        b = result
    return result
