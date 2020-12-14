# getrawić metodę get(), aby w przypadku pustej kolejki zwracała wyjątek.
# getrawić metodę put() w tablicowej implementacji kolejki, aby w przypadku przepełnienia kolejki zwracała wyjątek.
# Napisać kod testujący kolejkę.

class Queue:

    def __init__(self, size=5):
        self.n = size + 1  # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0  # pierwszy do pobrania
        self.tail = 0  # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n - 1) % self.n == self.tail

    def put(self, data):
        if self.is_full():
            raise ValueError("Queue is full!")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")
        data = self.items[self.head]
        self.items[self.head] = None  # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data


import unittest


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue4 = Queue(4)

    def test_put_and_get(self):
        self.assertTrue(self.queue4.is_empty())
        self.queue4.put(1)
        self.assertFalse(self.queue4.is_empty())
        self.queue4.put(22)
        self.queue4.put(3)
        self.queue4.put(4)
        self.assertTrue(self.queue4.is_full())

        try:
            self.queue4.put(5)
        except Exception as ex:
            self.assertEqual(ValueError, ex.__class__)

        self.assertEqual(1, self.queue4.get())
        self.assertEqual(22, self.queue4.get())
        self.assertEqual(3, self.queue4.get())
        self.assertEqual(4, self.queue4.get())
        self.assertTrue(self.queue4.is_empty())

        try:
            self.queue4.get()
        except Exception as ex:
            self.assertEqual(ValueError, ex.__class__)

    def tearDown(self):
        pass
