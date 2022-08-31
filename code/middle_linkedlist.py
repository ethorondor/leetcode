'''
middle of the linkedlist
'''
#%%
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
    def find_middle_of_linkedlist(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse_linkedlist(self,head):
        prev = None
        while head:
            _tmp = head.next
            head.next = prev
            prev = head
            head = _tmp
        return prev
    
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

l = head.reverse_linkedlist(head)
# %%
