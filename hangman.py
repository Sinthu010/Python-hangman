import random
import string


from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    #print(word)
    word_letters = set(word) # letters in the word
    print("There are {} letters in the word".format(len(word)))
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    # getting user input
    count = 0
    while count < 10:

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            count += 1
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Correct!")
                print("{} more letters to guess!".format(len(word_letters)))
                if len(word_letters) == 0:
                    print("You guessed all the letters! You win!")
                    break
            else:
                print("Sorry that letter is not in the word. Try again!") ## print no of go's left
            print("You have {} go's left!".format(10 - count))
        elif user_letter in used_letters:
            print("You have already used that letter, try again")

        else:
            print("Letter not recognised. Please try again")
    else:
        print("You're out of go's! The word was: {}".format(word) )

hangman()
