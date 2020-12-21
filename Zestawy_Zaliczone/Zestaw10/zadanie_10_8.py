# Stworzyć ADT w postaci kolejki losowej, z której elementy będą pobierane w losowej kolejności.
# Zadbać o to, aby każda operacja była wykonywana w stałym czasie, niezależnie od liczby elementów w kolejce.

import random


class RandomQueue:

    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        ''' zwraca losowy element '''
        if self.is_empty():
            raise ValueError("Queue is empty!")
        length = len(self.items)
        r = random.randint(0, length - 1)
        tmp = self.items[r]
        self.items[r] = self.items[length - 1]
        self.items[length - 1] = tmp
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return False

    def clear(self):
        ''' czyszczenie listy '''
        self.items = []


import unittest


class TestRandomQueue(unittest.TestCase):
    def setUp(self):
        self.randQueue = RandomQueue()

    def test_insert_and_remove(self):
        self.assertTrue(self.randQueue.is_empty())
        self.randQueue.insert(1)
        self.assertFalse(self.randQueue.is_empty())
        self.randQueue.insert(2)
        self.randQueue.insert(3)
        self.randQueue.insert(4)

        removed = set()
        for i in range(4):
            print(self.randQueue.items)
            removed.add(self.randQueue.remove())
            print(removed)

        self.assertEqual({1, 2, 3, 4}, removed)

        self.assertTrue(self.randQueue.is_empty())

        try:
            self.randQueue.remove()
        except Exception as ex:
            self.assertEqual(ValueError, ex.__class__)

    def tearDown(self):
        pass
