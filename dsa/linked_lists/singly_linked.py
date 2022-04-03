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

    def __contains__(self, key):
        return True if key in [node.val for node in self] else False

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

    @staticmethod
    def __verify_node(val):
        return ListNode(val) if not isinstance(val, ListNode) else val

    def is_empty(self):
        return not self.__head

    def prepend(self, val):
        new_node = self.__verify_node(val) 
        if self.is_empty():
            self.__head = self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head = new_node
        self.__size += 1
        
    def append(self, val):
        self.__tail = new_node = self.__verify_node(val) 
        if self.is_empty():
            return self.prepend(new_node)
        
        curr = self.__head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        self.__size += 1

    def insert_nth(self, val, index):
        if index > self.__size:
            raise IndexError("Index out of range")
        if index == 0:
            return self.prepend(val)
        if index == self.__size:
            return self.append(val)

        new_node, position = self.__verify_node(val), 0
        curr, prev = self.__head, None

        while curr and position != index:
            prev, curr = curr, curr.next
            position += 1

        prev.next, new_node.next = new_node, curr
        self.__size += 1

    def insert_before(self, index):
        pass

    def insert_after(self, index):
        pass

    def delete_nth(self, index):
        pass

    def delete_head(self):
        curr = self.__head
        self.__head, curr = self.head.next, None
        self.__size -= 1

    def delete_tail(self):
        if self.is_empty():
            return
        if self.__size == 1:
            return self.delete_head()

        curr, prev = self.__head, None
        while curr.next:
            prev, curr = curr, curr.next
        self.__tail, prev.next = prev, curr.next
        curr = None
        self.__size -= 1

    def delete(self, key):
        if self.is_empty():
            return
        if self.__head.val == key:
            return self.delete_head()
        if self.__tail.val == key:
            return self.delete_tail()

        curr, prev = self.__head, None
        while curr:
            if curr.val == key:
                prev.next, curr = curr.next, None
                self.__size -= 1
                return
            prev, curr = curr, curr.next

    def search(self, key):
        pass
    

