#%%
'''
palindrome linked list
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_middle(head):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

def reverse_linkedlist(head):
    prev = None
    current = head
    while current:
        _tmp = current.next
        current.next = prev
        prev = current
        current = _tmp
    return prev

def is_palindrome_linkedlist(head):
    slow = reverse_linkedlist(find_middle(head))
    left = head
    right = slow
    while right:
        if right.value != left.value:
            return False
        right = right.next
        left = left.next 
    return True
    

head = Node(1)
head.next = Node(2)
is_palindrome_linkedlist(head)
# %%
