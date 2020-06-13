class Node(object):

    def __init__(self, value):
        self.value = value

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev

    def insert(self, prev, next):
        self.prev = prev
        self.next = next
        self.next.prev = self
        self.prev.next = self


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.start = Node(None)
        self.end = Node(None)
        self.start.next = self.end
        self.end.prev = self.start
        self.capacity = capacity
        self.size = 0
        self.cache = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache or self.cache[key].value is None:
            return -1
        else:
            node = self.cache[key]
            node.remove()
            node.insert(self.start, self.start.next)
            return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.cache or self.cache[key].value is None:
            if self.size < self.capacity:
                self.size = self.size + 1
            else:
                lru_node = self.end.prev
                lru_node.value = None
                lru_node.remove()
            new_node = Node(value)
            self.cache[key] = new_node
            new_node.insert(self.start, self.start.next)
        else:
            key_node = self.cache[key]
            key_node.value = value
            key_node.remove()
            key_node.insert(self.start, self.start.next)



def main():
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    print cache.get(1)
    cache.put(3, 3)
    print cache.get(2)
    cache.put(4, 4)
    print cache.get(1)
    print cache.get(3)
    print cache.get(4)


if __name__ == '__main__':
    main()
