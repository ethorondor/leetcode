'''
start of the linkedlist cycle
'''
#%%
class node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
        
def start_of_linkedlist(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            curr = slow
            length = length_of_cycle(curr)
            break
    p1 = head
    p2 = head
    for i in range(length):
        p2 = p2.next
        
    while p1 != p2:
        p1=p1.next
        p2=p2.next
    return p1
    
def length_of_cycle(head):
    p1 = head
    p2 = head.next
    l = 1
    while p1 != p2:
        p2 = p2.next
        l += 1
    return l
head = node(1)
head.next = node(2)
head.next.next = node(3)
head.next.next.next = node(4)
head.next.next.next.next = node(5)
head.next.next.next.next.next = head.next.next
h = start_of_linkedlist(head)
# %%
