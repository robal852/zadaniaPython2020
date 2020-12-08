class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)  # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0  # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        # return self.length == 0
        return self.head is None

    def count(self):  # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:  # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):  # klasy O(N)
        if self.head:  # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):  # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:  # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None  # czyszczenie łącza
        self.length -= 1
        return node  # zwracamy usuwany node

    # ... inne metody ...

    def remove_tail(self):  # klasy O(N)
        ''' Zwraca cały węzeł, skraca listę. Dla pustej listy rzuca wyjątek ValueError. '''
        if self.is_empty():
            raise ValueError("pusta lista")
        removed = self.tail
        if self.head == self.tail:  # self.length == 1
            self.head = self.tail = None
        else:
            node = self.head
            while node.next.next:
                node = node.next
            node.next = None
            self.tail = node
        self.length -= 1
        return removed

    def merge(self, other):  # klasy O(1)
        ''' Węzły z listy other są przepinane do listy self na jej koniec. Po zakończeniu operacji lista other ma być pusta. '''
        if other.is_empty():
            raise ValueError("pusta lista")
        if self != other:
            self.tail.next = other.head
            self.tail = other.tail
            self.length += other.length
            other.head = None
            other.tail = None
            other.length = 0

    def clear(self):
        ''' czyszczenie listy '''
        self.head = None
        self.tail = None
        self.length = 0

    def search(self, data):  # klasy O(N)
        '''  Zwraca łącze do węzła o podanym kluczu lub None. '''
        node = self.head
        while node != None:
            if node.data == data:
                return node
            node = node.next
        return None

    def find_min(self):  # klasy O(N)
        ''' Zwraca łącze do węzła z najmniejszym kluczem lub None dla pustej listy.'''
        if self.is_empty():
            return None
        min = self.head
        node = self.head
        while node != None:
            if node.data < min.data:
                min = node
            node = node.next
        return min

    def find_max(self):  # klasy O(N)
        ''' Zwraca łącze do węzła z największym kluczem lub None dla pustej listy.'''
        if self.is_empty():
            return None
        max = self.head
        node = self.head
        while node != None:
            if node.data > max.data:
                max = node
            node = node.next
        return max

    def reverse(self):  # klasy O(N)
        ''' Odwracanie kolejności węzłów na liście. '''
        node = self.head
        before = None
        while node:
            tmp = node.next
            node.next = before
            before = node
            node = tmp
        node = self.tail
        self.tail = self.head
        self.head = node




alist = SingleList()
alist.insert_head(Node(11))  # [11]
alist.insert_tail(Node(22))  # [22, 11]
alist.insert_tail(Node(33))  # [11, 22, 33]

blist = SingleList()
blist.insert_head(Node(44))  # [44]
blist.insert_tail(Node(55))  # [44, 55]
blist.insert_tail(Node(66))  # [44, 55, 66]

blist.reverse() # [66, 55, 44]
alist.merge(blist)  # [11, 22, 33] + [66, 55, 44]

print("find_min [11, 22, 33, 66, 55, 44] = {}".format(alist.find_min()))
print("find_max [11, 22, 33, 66, 55, 44] = {}".format(alist.find_max()))
print("search 11 = {}".format(alist.search(11)))
print("search 100 = {}\n".format(alist.search(100)))


while not alist.is_empty():
    print("length {}".format(alist.length))
    print("remove tail {}".format(alist.remove_tail()))


clist = SingleList()
clist.insert_head(Node(1))
clist.clear()
print("\ndlugosc clist po clear:", clist.count())