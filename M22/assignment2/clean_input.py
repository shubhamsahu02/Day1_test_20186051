'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
	s = ""
	for i in string:
    regex = re.compile('[^a-z]')
    return [regex.sub('', eachword.strip()) for eachword in inp_str.lower().split(' ')]

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
