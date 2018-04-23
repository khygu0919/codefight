'''
Check if the given string is a correct time representation of the 24-hour clock.

Example

For time = "13:58", the output should be
validTime(time) = true;
For time = "25:51", the output should be
validTime(time) = false;
For time = "02:76", the output should be
validTime(time) = false.
'''
def validTime(time):
    if 24>int(time[0:2])>1 and 61>int(time[3:])>=0:
        return True
    return False
time='25:51'
print validTime(time)