'''Assume s is a string of lower case characters.
Number of times bob occurs is: 2'''

COUNT = 0
S_V = input()
S_V2 = 'bob'
for i in range(len(S_V)):
    if S_V2 == S_V[i:i+3]:
        COUNT += 1
print(COUNT)
