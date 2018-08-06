"""Exercise: fourth power
# This function takes in one number and returns one number."""
def square(x_x):
    '''
    x_x: int or float.
    '''
    # Your code here
    return x_x*x_x


def fourth_power(x_x):
    '''
    x_x: int or float.'''
    return square(square(x_x))

def main():
    """function"""
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(fourth_power(int(float(str(data)))))
    else:
        print(fourth_power(data))

if __name__ == "__main__":
    main()
