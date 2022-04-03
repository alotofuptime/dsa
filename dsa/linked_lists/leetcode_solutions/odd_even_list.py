from typing import Optional
from dsa.linked_lists.singly_linked import LinkedList, ListNode

# https://leetcode.com/problems/odd-even-linked-list/

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_head, odd_head = ListNode(-1), ListNode(-1)
        even_ptr, odd_ptr = even_head, odd_head
        curr, pos = head, 1
        while curr:
            nxt = curr.next
            curr.next = None
            if pos % 2 == 0:
                even_ptr.next = curr
                even_ptr = even_ptr.next
            else:
                odd_ptr.next = curr
                odd_ptr = odd_ptr.next
            curr = nxt
            pos += 1
        odd_ptr.next = even_head.next
        return odd_head.next
