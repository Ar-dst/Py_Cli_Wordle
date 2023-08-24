import os
import random

#=======================================

info = '''
Welcome to Wordle

This is a simple game where you have six turns and in your turn you can enter a five-letter English word.
I have already chosen a word and I will guide you based on it.
If that letter from your word does not exist in my word, it is recorded under *, if it exists but is not there, it is recorded under - and if it is there, it is recorded under ^.
If you can guess my word in six turns, you win, and if you can't, you lose.
Press Enter to start the game.
'''
#=======================================

def game():

    print('game started, enter your guess\n\n')
    words = (open(r'words.txt', 'r').readlines())
    for i in range (len(words)): words[i] = words[i].strip()

    select = random.randint(0, len(words))

    for i in range(6):
        while True:
            word = str(input('')).lower()
            if word == '':
                print('\nPlease enter word\n')
            elif word.isalpha() == False:
                print('\nYour word is not accepted!\n')            
            elif len(word) < 5:
                print('\nword is so small!\n')
            elif len(word) > 5:
                print('\nword is so big!\n')
            elif not word in words:
                print('\nYour word does not exist in our dictionary!\n')
            elif len(word) == 5:
                break
                #TODO fix problem
        status = ''
        for i in range(5):
            if words[select][i] == word[i]:
                status += '^'
            else:
                if word[i] in words[select]:
                    status += '-'
                else:
                    status += '*'
        if status == '^^^^^':
            print('YOU WIN  The answer is "', words[select], '"')

            words.close()
        else:
            print(status, end='')
        print('\n')
            
    print('You loose  The answer is "', words[select], '"')

    words.close()


    
#=======================================

def start():

    for i in range(os.get_terminal_size().lines): print('\n')

    print(info, end='')

    input('')

    for i in range(os.get_terminal_size().lines): print('\n')

    game()

    yesno = str(input('play again?(n/Y): ')).lower()

    if yesno == 'no':

        print('\nGoodbye!!!\n')

        exit()
    elif yesno == 'n':

        print('\nGoodbye!!!\n')

        exit()
    else:
        game()

#=======================================
try:
    start()
except:

    yesno = str(input('play again?(n/Y): ')).lower()

    if yesno == 'no':

        print('\nGoodbye!!!\n')

        exit()
    elif yesno == 'n':

        print('\nGoodbye!!!\n')

        exit()
    else:
        game()
