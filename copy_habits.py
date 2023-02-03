"""
copies habits from a "habits" page into the currently selected section
author- Dan Scarafoni
dan@scarafoni.com
"""


habits = open('/home/dan/Documents/Personal WIki/Life_Goals/Current_Habits.txt', 'r').read()
habits = '\n'.join(habits.split('\n')[7:-1])
print(habits)