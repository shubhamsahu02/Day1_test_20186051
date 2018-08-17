'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math


def clean(input_string):
    input_string = input_string.lower()
    regex = re.compile('[^a-z ]')
    input_string = regex.sub('', input_string)
    list_of_words = input_string.split(' ')
    for each_word_index in range(len(list_of_words)):
        list_of_words[each_word_index] = list_of_words[each_word_index].strip()
    return list_of_words

def remove_stop(list_of_words):
    stop_words = load_stopwords('stopwords.txt')
    for each_word in list_of_words:
        if each_word in stop_words:
            list_of_words.remove(each_word)
    return list_of_words

def word_freq(list_of_words, index, dictionary):
    for each_word in list_of_words:
        if each_word !="" and each_word not in dictionary:
            dictionary[each_word] = [0,0]
        dictionary[each_word][index] += 1
    return dictionary

def computation(dictionary):
    numerator = sum(value[0]*value[1] for value in dictionary.values())
    denominator1 = math.sqrt(sum(value[0]**2 for value in dictionary.values()))
    denominator2 = math.sqrt(sum(value[1]**2 for value in dictionary.values()))
    return numerator / (denominator1*denominator2)

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    input_1 = clean(dict1)
    input_2 = clean(dict2)

    input_1 = remove_stop(input_1)
    input_2 = remove_stop(input_2)

    dictionary = {}
    dictionary = word_freq(input_1, 0, dictionary)
    dictionary = word_freq(input_2, 1, dictionary)
    return computation(dictionary)


def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
