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
    
  second = slow.next 
  prev = None
  slow.next = None
  while second:
    tmp = second.next 
    second.next = prev 
    prev = second 
    second = tmp
  first = head 
  second = prev 
  while second:
    tmp1 = first.next
    tmp2 = second.next
    first.next = second
    second.next = tmp1
    first = tmp1
    second = tmp2
  



head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(12)
reorder(head)
head.print_list()

# %%
