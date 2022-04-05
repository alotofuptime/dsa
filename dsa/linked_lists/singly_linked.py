from typing import Any, Optional

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.__head = head if not head else ListNode(head)
        self.__size = 0 if not head else 1

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, data):
        self.__head = data
        self.__size += 1

    @property
    def size(self):
        return self.__size
