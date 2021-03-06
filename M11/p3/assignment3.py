# Assignment-3
'''
At this point, we have written code to generate a random hand and display that hand to the user.
# We can also ask the user for a word (Python's input) and score the word (using your getWordScore).
'''

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function

    count = 0
    for char in word:
        if char in hand:
            count += 1
    if count == len(word):
        if word in word_list:
            return True
    return False

def main():
    """function"""
    word = input()
    n_e = int(input())
    adict = {}
    for _ in range(n_e):
        data = input()
        l_l = data.split()
        adict[l_l[0]] = int(l_l[1])
    l2_h = input().split()
    print(is_valid_word(word, adict, l2_h))
if __name__ == "__main__":
    main()
