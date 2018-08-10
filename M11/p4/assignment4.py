#Exercise: Assignment-4
#We are now ready to begin writing the code that interacts with the player.
#We'll be implementing the playHand function. This function allows the user to play out a single hand.
#First, though, you'll need to implement the helper calculateHandlen function, which can be done in under five lines of code.


def calculate_hand_len(hand):
    """
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    sum_val = 0
    for key_dict in hand:
        sum_val += hand[key_dict]
    return sum_val

def main():
    """function"""
    n_n = input()
    adict = {}
    for _ in range(int(n_n)):
        data = input()
        l_l = data.split()
        adict[l_l[0]] = int(l_l[1])
    print(calculate_hand_len(adict))

if __name__ == "__main__":
    main()