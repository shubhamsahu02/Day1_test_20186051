# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998
"""Square root bisection"""
# testcase 2
# input: 49
# output: 6.999999999999991
INPUT_STRING = int(input())
EPSI_LON = 0.01
LOW = 0
HIGH = INPUT_STRING
GUESS = (LOW+HIGH)/2
while abs(GUESS**2-INPUT_STRING) >= EPSI_LON:
    if GUESS**2 > INPUT_STRING:
        HIGH = GUESS
    else:
        LOW = GUESS
    GUESS = (LOW+HIGH)/2
print(GUESS)
