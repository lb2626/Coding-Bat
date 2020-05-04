"""

Given a string, return a string where for every char in the original, there are two chars.


double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'

Each time the loop steps through the string we add to the result and times it by 2.

"""

def double_char(str):
  
  result = ''
  
  for i in range(0,len(str), 1):
    result = result + str[i]  * 2
  return result