'''
merged k sorted list
using heap to solve this problem
'''
#%%
from heapq import *

class list_node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        