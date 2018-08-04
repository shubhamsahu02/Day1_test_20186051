'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    '''
Read number from the input, store it in variable int_input.'''
    num = int(input())
    product = 1
    rem = 0
    a_b = 1
    if num < 0:
        a_b = -1
        num = abs(num)
    else:
        a_b = 1
    if num != 0:
        while num >= 1:
            rem = num%10
            product = int(product) * int(rem)
            num = num//10
        print(product*a_b)
    else:
        print("0")

if __name__ == "__main__":
    main()
