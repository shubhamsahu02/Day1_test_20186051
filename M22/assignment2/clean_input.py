'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    s = ""

    for i in string:
        s = re.sub('[^A-Za-z0-9]','', string.lower())


   # regex = re.compile('[^A-Za-z0-9]')
   #return [regex.sub('', eachword.strip()) for eachword in string.lower().split(' ')]

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
