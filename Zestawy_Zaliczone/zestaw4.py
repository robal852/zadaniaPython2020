# Zestaw zadan 4.
# Albert Surmacz
# 28.10.2020

# Zadanie 4.2
# Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, które zwracają pełny string przez return.

def tape(x):
    '''Zadanie 3.5 jako funkcja.'''
    length = x
    tape = ""
    for i in range(int(length)):
        tape += "|"
        numOfDots = 3 + len(str(length))
        for j in range(numOfDots):
            tape += "."
    tape += "|\n"
    for i in range(int(length)):
        tape += str(i)
        numOfSpaces = (4 + (len(str(length)) - len(str(i))))
        for j in range(numOfSpaces):
            tape += " "
    lenOfLastDigit = len(str(length))
    if (lenOfLastDigit > 1):
        tape = tape[:-lenOfLastDigit + 1]
    tape += str((int(length)))
    return (tape)


def matrix(x, y):
    '''Zadanie 3.6 jako funkcja.'''
    if (x < 1 or y < 1):
        return
    rysunek = ""
    for i in range(x):
        for j in range(y):
            rysunek += "+---"
        rysunek += "+\n"
        for j in range(y):
            rysunek += "|   "
        rysunek += "|\n"
    for j in range(y):
        rysunek += "+---"
    rysunek += "+\n"
    return (rysunek)


# Zadanie 4.3
# Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.
def factorial(n):
    '''Silnia iteracyjnie.'''
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Zadanie 4.4
# Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.
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


# Zadanie 4.5
# Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie.
# Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.

def odwracanie(L, left, right):
    '''Odwracanie iteracyjne.'''
    for i in range(len(L)):
        if i < left:
            pass
        elif i >= left and i < right:
            tmp = L[i]
            L[i] = L[right]
            L[right] = tmp
            right -= 1
        else:
            pass
    return L


# Zadanie 4.6
# Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która może zawierać zagnieżdżone podsekwencje.
# Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).
def sum_seq(sequence):
    '''Suma liczb zawartych w sekwencji rekurencyjnie.'''
    sum = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            sum += sum_seq(item)
        else:
            sum += item
    return sum


# ZADANIE 4.7
# Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami,
# a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości.
# Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji.
# Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).
# seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
# print flatten(seq)            # [1,2,3,4,5,6,7,8,9]
def flatten(sequence):
    '''Splaszczona lista rekurencyjnie.'''
    result = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result += flatten(item)
        else:
            result += str(item)
    return result


if __name__ == "__main__":
    print(tape(12))
    print(matrix(2, 4))
    print(factorial(5))
    print(fibonacci(5))
    print(odwracanie([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 5))
    print(sum_seq([[1, (1, 1, 1)], [1], (1, 1), [1, 1], (1, 1, 1)]))
    print(flatten([1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]))
