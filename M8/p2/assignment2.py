'''Write a Python function, sumofdigits, that takes in one number and
returns the sum of digits of given number.
This function takes in one number and returns one number.
'''
def sumofdigits(num_ber):
    '''sub function'''

    if num_ber == 0:
        return 0
    return(num_ber % 10) + sumofdigits(num_ber // 10)
def main():
    """defining main"""
    in_put = input()
    print(sumofdigits(int(in_put)))

if __name__ == "__main__":
    main()
