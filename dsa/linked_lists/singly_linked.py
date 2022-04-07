from typing import Any, Optional

class ListNode:
    def __init__(self, data=0, next=None):
        self.__data = data
        self.__next = ListNode(next) if next and not isinstance(next, ListNode) else next

    @property
    def data(self):
        return self.__data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, data):
        self.__next = ListNode(data) if not isinstance(data, ListNode) else data

    def __repr__(self):
        return f"Node({self.__data})"


class LinkedList:
    def __init__(self, head=None):
        self.__head = ListNode(head) if head and not isinstance(head, ListNode) else head
        self.__size = 0 if not head else 1

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, data):
        data = ListNode(data) if not isinstance(data, ListNode) else data
        self.__head = data
        self.__size += 1

    @property
    def size(self):
        return self.__size
