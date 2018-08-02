#Assume s is a string of lower case characters.
'''Number of vowels: 5'''
def main():
    """"program for vowels"""
    var_s = input()
    count = 0
    for char in var_s:
        if char in 'AEIOUaeiou':
            count = count+1
    print(count)
if __name__ == "__main__":
    main()
