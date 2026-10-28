class ListNode:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None
        self.before = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} # key value pairs, value wil be a listnode
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.before = self.head

    def get(self, key):
        if key not in self.cache:
            return -1
        self.removeNode(self.cache[key])
        self.addNode(self.cache[key])
        return self.cache[key].value

    def put(self, key, value):
        if key in self.cache: 
            node = self.cache[key]
            node.value = value
            self.removeNode(node)
            self.addNode(node)
        else:
            newNode = ListNode(key,value)
            self.cache[key] = newNode
            self.addNode(newNode)
        
        if len(self.cache) > self.capacity:
            n = self.tail.before
            del self.cache[n.key]
            self.removeNode(n)


    def addNode(self, node):
        node.before = self.head
        node.next = self.head.next
        self.head.next.before = node
        self.head.next = node

    def removeNode(self, node):
        node.before.next = node.next
        node.next.before = node.before

    