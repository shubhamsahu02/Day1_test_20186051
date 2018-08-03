# Write a python program to find the square root of the given number
# using newton raphson method

# testcase 1
# input: 25
# output: 4.999999999999998
"""Newton Raphson method"""
INPUT = int(input())
EPSILON = 0.01
GUESS = INPUT/2.0
while GUESS <= INPUT:
    if abs(GUESS**2-INPUT) >= EPSILON:
        GUESS = GUESS-(GUESS**2 - INPUT)/(2*GUESS)
    else:
        break
print(GUESS)
