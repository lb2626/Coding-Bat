"""

We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.


parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False

My take home -> If the first statement is not true the second statement will not be evaluated...
"""

def parrot_trouble(talking, hour):
  return talking == True and (hour < 7 or hour > 20)
