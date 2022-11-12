'''
reverse a linkedlist
'''
#%%
class node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
def reverse(head):
    if not head:
        return head
    prev = None
    curr = head
    while curr:
        _temp = curr.next
        curr.next = prev
        prev = curr
        curr = _temp
    return prev 

head = node(1)
head.next = node(2)
head.next.next = node(3)
head.next.next.next = node(4)
reverse(head)
# %%
