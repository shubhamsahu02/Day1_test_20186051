'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
STR_ING = ""
S_1= int(input())

for i in range(S_1):
    STR_ING += input() +'\n'
    i += 1
print (STR_ING)


def main():
    pass

if __name__ == '__main__':
    main()

