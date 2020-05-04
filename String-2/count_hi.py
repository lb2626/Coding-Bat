"""

Return the number of times that the string "hi" appears anywhere in the given string.


count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2

Remember for i in range(0, len(str) - (<reading frame size> -1, 1) 
                                            'hi' is 2 so 2-1 = 1 - 1
"""

def count_hi(str):

  count = 0
  for i in range(0, len(str)-1, 1):
    if str[i:i+2] == 'hi':
      count = count + 1
    
  return count
      