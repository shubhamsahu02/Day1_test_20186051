def main():
   print('Think of a number between 0 to 100')
   low=0
   high=100
   while True:
       guess=(high+low)//2
       user = input('Is your secret number ' + str(guess) + '\n'
               + 'Enter "h" to indicate the guess is too high. '
               + 'Enter "l" to indicate the guess is too low. '
               + 'Enter "c" to indicate I guessed correctly. ')
       if user == 'h':
           low=guess
       elif user == 'l':
           high=guess
       elif user == 'c':
           print('Game over.Your secret number is :'+str(guess))
           break
       else:
           print('Invalid entry')
       guess=(high+low)//2
if __name__== "__main__":
   main()