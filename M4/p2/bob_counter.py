'''Assume s is a string of lower case characters.
Number of times bob occurs is: 2'''

COUNT = 0
inp_str = input()
comp_str = 'bob'
for i in range(len(inp_str)):
    if comp_str == inp_str[i:i+3]:
        COUNT += 1
print(COUNT)
