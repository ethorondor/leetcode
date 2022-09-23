'''
middle of the linkedlist
'''
#%%
class node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
def find_middle_of_linkedlist(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    
head = node(1)
head.next = node(2)
head.next.next = node(3)
head.next.next.next = node(4)
head.next.next.next.next = node(5)
s = find_middle_of_linkedlist(head)
# %%
