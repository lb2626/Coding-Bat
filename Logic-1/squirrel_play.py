"""

The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.


squirrel_play(70, False) → True
squirrel_play(95, False) → False
squirrel_play(95, True) → True



So if it's the summer, we return true if the temperature is between 60 and 100 degrees with is a new upper limit.
Otherwise, we will return the normal temperature ranges. And that's all we need to return to pass the test cases.


"""


def squirrel_play(temp, is_summer):
  if is_summer:
    return 60 <= temp <= 100
  return 60 <= temp <= 90
