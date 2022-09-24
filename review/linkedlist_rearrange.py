'''
rearrange linkedlist
'''
#%%
from __future__ import print_function
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(str(temp.value) + " ", end='')
      temp = temp.next
    print()


def reorder(head):
  if head is None or head.next is None:
    return

  # find middle of the LinkedList
  slow = head
  fast = head.next
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    
  second_half = reverse(slow.next)
  first_half = head
  
  while second_half:
    tmp1 = first_half.next
    tmp2 = second_half.next
    first_half.next = second_half
    second_half = tmp1
    first_half = tmp1
    second_half = tmp2
  
      
def reverse(head):
  prev = None
  while head is not None:
    next = head.next
    head.next = prev
    prev = head
    head = next
  return prev



head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(12)
reorder(head)
head.print_list()

# %%
