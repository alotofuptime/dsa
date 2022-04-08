from typing import Any, Optional

class ListNode:

    @classmethod
    def parse_data(cls, data):
        if not data:
            return 0
        elif data and isinstance(data, ListNode):
            return data.data
        else:
            return data

    def __init__(self, data=0, next=None):
        self.__data = self.parse_data(data)
        self.__next = ListNode(next) if next and not isinstance(next, ListNode) else next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = self.parse_data(data)

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, data):
        self.__next = ListNode(data) if not isinstance(data, ListNode) else data

    def __repr__(self):
        return f"Node({self.__data})"


class LinkedList:

    @classmethod
    def parse_head(self, data: Any) -> Optional[ListNode]:
        node = ListNode(data) if data and not isinstance(data, ListNode) else data
        return node

    def __init__(self, head=None):
        self.__head = self.parse_head(head)
        self.__size = 0 if not head else 1
        #TODO refactor this if else block & make it a method
        #TODO make tail private
        if self.__head and self.__head.next:
            self.__size += 1
            self.tail = self.__head.next
        else:
            self.tail = self.__head

    @property
    def head(self):
        return self.__head

    @head.setter
    #TODO test setting head to null val
    def head(self, data):
        data = ListNode(data) if not isinstance(data, ListNode) else data
        self.__head = data
        self.__size += 1
        self.tail = self.__head

    @property
    def size(self):
        return self.__size
