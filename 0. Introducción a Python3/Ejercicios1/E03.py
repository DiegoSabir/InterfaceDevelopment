"""
Given a number in seconds, perform the transformation into hours, minutes, and seconds.
Repeat the exercise in reverse: given a number in hours, minutes, and seconds, 
transform it into seconds.
"""

hours = 0
minutes = 0
seconds = int(input("Enter an amount in seconds:"))

while seconds >= 3600:
    hours += 1
    seconds -= 3600

while seconds >= 60:
    minutes += 1
    seconds -= 60

print("Hours:", hours, "Minutes:", minutes, "Seconds:", seconds)
