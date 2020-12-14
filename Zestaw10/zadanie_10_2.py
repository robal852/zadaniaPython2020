# Poprawić implementację tablicową stosu tak, aby korzystała z wyjątków w przypadku pojawienia się błędu.
# Metoda pop() ma zgłaszać błąd w przypadku pustego stosu.
# Metoda push() ma zgłaszać błąd w przypadku przepełnienia stosu.
# Napisać kod testujący stos.


class Stack:

    def __init__(self, size=10):
        self.items = size * [None]  # utworzenie tablicy
        self.n = 0  # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise ValueError("Stack is full. Can't push ", + data)
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.size == 0:
            raise ValueError("Stack is empty. Can't pop.")
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None  # usuwam referencję
        return data


import unittest


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack4 = Stack(4)

    def test_push_and_pop(self):
        self.assertTrue(self.stack4.is_empty())
        self.stack4.push(1)
        self.assertFalse(self.stack4.is_empty())
        self.stack4.push(22)
        self.assertEqual(2, self.stack4.n)
        self.stack4.push(3)
        self.stack4.push(4)
        self.assertTrue(self.stack4.is_full())

        try:
            self.stack4.push(5)
        except Exception as ex:
            self.assertEqual(ValueError, ex.__class__)

        self.assertEqual(4, self.stack4.pop())
        self.assertEqual(3, self.stack4.pop())
        self.assertEqual(22, self.stack4.pop())
        self.assertEqual(1, self.stack4.pop())
        self.assertTrue(self.stack4.is_empty())

        try:
            self.stack4.pop()
        except Exception as ex:
            self.assertEqual(ValueError, ex.__class__)

    def tearDown(self):
        pass
