'''
start of a linkedlist cycle
find the start of linkedlist cycle
'''
#%%
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
def length_linkedlist_cycle(head):
    # find the length of the cycle
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            count = 0
            current = slow
            while True:
                count += 1
                slow = slow.next
                if slow == current:
                    return count
    return 0

def start_linkedlist_cycle(head):
    cycle_len = length_linkedlist_cycle(head)
    if len == 0:
        return None
    fast = head
    slow = head
    for i in range(cycle_len):
        fast = fast.next
    while True:
        if fast == slow:
            return fast
        fast = fast.next
        slow = slow.next

 
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

head.next.next.next.next.next.next = head
start = start_linkedlist_cycle(head)
# %%
