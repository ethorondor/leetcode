'''
is a linkedlist palindrome
'''
#%%
class node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
def is_palindrome(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    reversed_second_half = reverse_linkedlist(slow)
    first_half = head
    while reversed_second_half and first_half:
        if reversed_second_half.value == first_half.value:
            reversed_second_half = reversed_second_half.next
            first_half = first_half.next
        else:
            return False
    return True

def reverse_linkedlist(head):
    curr = head
    res = None
    while curr:
        _tmp = curr.next
        curr.next = res
        res = curr
        curr = _tmp
    return res
        

head = node(1)
head.next = node(2)
head.next.next = node(3)
head.next.next.next = node(2)
head.next.next.next.next = node(1)
is_palindrome(head)
# %%
