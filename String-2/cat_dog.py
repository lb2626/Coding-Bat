"""
Return True if the string "cat" and "dog" appear the same number of times in the given string.


cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True


Utilizing the reading frame concept so the len of the str should be -2 because 3 - 1 = 2

"""

def cat_dog(str):
  
  dog_count = 0
  cat_count = 0
  
  for i in range(0, len(str)-2, 1):
    if str[i:i+3] == 'dog':
      dog_count += 1
    if str[i:i+3] == 'cat':
      cat_count += 1
  return dog_count == cat_count