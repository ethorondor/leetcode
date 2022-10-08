'''
reverse to make equal
'''
def are_they_equal(array_a, array_b):
      # Write your code here
  hash_table = {}
  for n in array_a:
    if n in hash_table:
      hash_table[n] +=1
    hash_table[n] = 1
  for n in array_b:
    if n in hash_table:
      hash_table[n] -= 1
    else:
      return False
  if sum(hash_table.values()) == 0:
    return True
  else:
    return False

are_they_equal([1,2,3,4],[1,3,2,4])