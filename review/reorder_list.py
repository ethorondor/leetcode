'''
reorder a singly linkedlist
'''
class node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
def find_mid(head):
    s = head
    f = head
    while f and f.next:
        s = s.next
        f = f.next.next 
        if s == f:
           return s
def reverse(head):
    prev = None
    curr = head
         
head = node(0)
head.next = node(1)
head.next.next = node(2)
head.next.next.next = node(3)
head.next.next.next.next = node(4)
head.next.next.next.next.next = node(5)