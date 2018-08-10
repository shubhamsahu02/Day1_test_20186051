'''
Exercise: Assignment-1
'''

def get_word_score(word, n_n):
    """
    Returns the score for a word. Assumes the word is a valid word.
    
The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see scrabble_values)

word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    scrabble_values = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    sum_0 = 0
    l_l = len(word)
    for j in word:
        if j in scrabble_values:
            sum_0 = sum_0 + scrabble_values[j]
    if n_n == l_l:
        sum_0 = sum_0 * l_l
        return sum_0 + 50
    return sum_0 * l_l
def main():
    '''
    Main function for the given problem
    '''
    data = input()
    data = data.split()
    print(get_word_score(data[0], int(data[1])))


if __name__ == "__main__":
    main()
