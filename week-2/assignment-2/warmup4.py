# Traceback (most recent call last):
# File "/Users/johnmartin0227/Documents/Workspace/Code the Dream/python-intro-homework/week-2/assignment-2/warmup4.py", line 1, in <module>
#     print(happy)
#           ^^^^^
# NameError: name 'happy' is not defined
# The error happened because I tried to 
# print a variable that doesn't exist. Since
# Python reads top to bottom, the variable happy
# was called when it didn't have an assignment yet.
#
# I defined happy to the integer 3 before the print.
# allowing it to print without error. Since happy
# exists, there is no more name error as happy
# is assigned 3
happy = 3
print(happy)