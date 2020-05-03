"""
Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'

My note: you don't need len(str), but it helps me reinforce the concept that the problem is 
trying to help you grasp. So here is how n is slicing the string. 
 123456
 kitten  missing_char("kitten")  => str[0:1] + str[2:6]
                                    str[0:n] + str[n +1:]

"""

def missing_char(str, n):
 return str[:n] + str[n+1: len(str)] 