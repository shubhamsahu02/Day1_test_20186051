'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string, lines):
	words = string.split()
	dict = {}
	for word in words:
		if word in dict:
			dict[word] += 1
		else:
			dict[word] = 1
	return dict






            
def main():
	lines = int(input)
	inp_string = input()
	text = ''.join(inp_string)
	text.split()
	print(tokenize(text))



    

if __name__ == '__main__':
    main()
