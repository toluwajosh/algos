"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def delink(l1):
    ord_list = []
    while l1.next is not None:
        ord_list.append(l1.val)
        l1 = l1.next
    ord_list.append(l1.val)
    return ord_list


def enlink(l1):
    old_list = ListNode(l1[-1])
    for i, l in enumerate(reversed(l1)):
        if i < 1:
            continue
        new_list = ListNode(l)
        new_list.next = old_list
        old_list = new_list
    return old_list


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ord_l1 = delink(l1)
        ord_l2 = delink(l2)
        carry_over = 0
        ord_sum_list = []
        new_len = max(len(ord_l1), len(ord_l2))
        for i in range(new_len):
            if i < len(ord_l1):
                x = ord_l1[i]
            else:
                x = 0
            if i < len(ord_l2):
                y = ord_l2[i]
            else:
                y = 0

            i_sum = x + y + carry_over
            if i_sum < 10:
                ord_sum_list.append(i_sum)
                carry_over = 0
            else:
                ord_sum_list.append(i_sum - 10)
                carry_over = 1
        if carry_over:
            ord_sum_list.append(carry_over)
        return enlink(ord_sum_list)


class SmallerSolution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            # divmod -> Return the tuple (x//y, x%y). Invariant: div*y + mod == x
            carry, out = divmod(val1 + val2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next
