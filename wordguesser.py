import random
import re

def wordselector():
    wordslist=[]
    file_path='/home/xav/Projects/Tryn/words.txt'
#using file to select from a large list of words
    with open(file_path, 'r') as file:
        for x in file:
            words = re.split(r'\s+', x.strip())
            wordslist.extend(words)

    guessword=random.choice(wordslist)
    return guessword
    #selecting a random word




def main():
    print("Welcome to Word Guesser")

    word=wordselector()
    guessedword=['-']*len(word)
    attempts=10

    while attempts > 0:
        print('\n Current Words are:'+' '.join(guessedword))
        guess=input('Guess a letter: ').lower()

        if guess in word:
            #updating 'guessword' if the word guessed is correct
            for i in range(len(word)):
                if word[i]==guess:
                    guessedword[i]=guess
                    print('Great Guess')
        else:
            attempts-=1
            print(f'Wrong Guess \n Remainig Attempts:{attempts}')
        if '-' not in guessedword:
            break
    if '-' not in guessedword:
        print("You guessed the word Correct!!!")
    else:
        print(f"Sorry you've run out of guesses \nThe word is:{word}")
    
main()
