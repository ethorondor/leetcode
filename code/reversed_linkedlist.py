#%%
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse_linkedlist(head):
    prev = None
    current = head
    while current:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
    return prev
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
ans = reverse_linkedlist(head)
# %%
