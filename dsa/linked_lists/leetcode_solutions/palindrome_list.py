from typing import Optional
from dsa.linked_lists.singly_linked import LinkedList, ListNode

class Solution:
    def is_palindrome_brute_force(self, head: Optional[ListNode]) -> bool:
        curr, vals = head, []

        while curr:
            vals.append(curr.val)
            curr = curr.next

        return vals[::-1] == vals
