"""
Given an int array length 2, return True if it contains a 2 or a 3.


has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False

Now I a just using conditional logic and checking whether or not a 2 or 3 are in 
a list of numbers.

"""

def has23(nums):
  if 2 in nums or 3 in nums:
    return True
  else:
    return False