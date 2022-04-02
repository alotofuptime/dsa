class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return f"Node({self.val})"

    def __str__(self):
        return self.__repr__()


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __iter__(self):
        curr = self.__head
        while curr:
            yield curr
            curr = curr.next

    def __len__(self):
        return self.size

    def __repr__(self):
        return " -> ".join([str(node.val) for node in self])

    def __str__(self):
        return self.__repr__()

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, val):
        return self.prepend(val)

    @property
    def tail(self):
        return self.__tail

    @tail.setter
    def tail(self, val):
        return self.append(val)

    @property
    def size(self):
        return self.__size

    def is_empty(self):
        return not self.__head

    def prepend(self, val):
        new_node = ListNode(val) if not isinstance(val, ListNode) else val
        if self.is_empty():
            self.__head = self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head = new_node
        self.__size += 1
        
    def append(self, val):
        self.__tail = new_node = ListNode(val) if not isinstance(val, ListNode) else val
        if self.is_empty():
            return self.prepend(new_node)
        
        curr = self.__head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        self.__size += 1

    def insert_nth(self, val, index):
        pass

    def insert_before(self, index):
        pass

    def insert_after(self, index):
        pass

    def delete_nth(self, index):
        pass

    def delete(self, key):
        pass

    def search(self, key):
        pass
    

