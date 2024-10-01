import random
import re
def wordselector():
    wordslist=[]
    file_path='/home/xav/Projects/Tryn/words.txt'
    with open(file_path, 'r') as file:
        for x in file:
            words=re.split(r'\s+',x.strip())
            wordslist.extend(words)
    guessword=random.choice(wordslist)
    return guessword
def main():
    print("Welcome to Word Guesser")
    word=wordselector()
    guessedword=['-']*len(word)
    attempts=10
    while attempts > 0:
        print('\n Current Words are:'+' '.join(guessedword))
        guess=input('Guess a letter: ').lower()
        if guess in word:
            for i in range(len(word)):
                if word[i]==guess:
                    guessedword[i]=guess
                    print('Great Guess')
        else:
            attempts-=1
            print('Wrong Guess')
        if '-' not in guessedword:
            break
    if '-' not in guessedword:
        print("You guessed the word Correct!!!")
    else:
        print("Sorry you've run out of guesses")
        print("The word is"+ word)
    
main()
