'''
reverse sub linkedlist
'''
#%%
class node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
def reverse_sublist(head, p, q):
    l_1 = head
    for i in range(p-1):
        l_1 = l_1.next
    l = l_1.next
    r = head
    for i in range(q):
        r = r.next
    r_tail = r.next 
    r.next = None
    prev = None
    curr = l
    while curr:
        _tmp = curr.next
        curr.next = prev
        prev = curr
        curr = _tmp
        
    l_1.next = prev
    l.next = r_tail
    return head

head = node(1)
head.next = node(2)
head.next.next = node(3)
head.next.next.next = node(4)
head.next.next.next.next = node(5)
l = reverse_sublist(head, 1, 3)
# %%
