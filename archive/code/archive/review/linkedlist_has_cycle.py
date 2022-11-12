'''
linkedlist has cycle
'''
#%%
class node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
        
def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False
    
    
head = node(1)
head.next = node(2)
head.next.next = node(3)
head.next.next.next = node(4)
head.next.next.next.next = node(5)
head.next.next.next.next.next = head.next.next
has_cycle(head)
# %%
