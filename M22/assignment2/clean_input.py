'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    '''function to remove special characters'''
    str_ing = ""

    for i in string:
        str_ing = re.sub('[^A-Za-z0-9]', '', string.lower())
        return str_ing

   # regex = re.compile('[^A-Za-z0-9]')
   #return [regex.sub('', eachword.strip()) for eachword in string.lower().split(' ')]

def main():
    '''function'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
