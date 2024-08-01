#Step 1 
import random
import hangman_art
import hangman_words

end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
lives = 6

print(f"{hangman_art.logo}\nWant to play a hangman?")
display = ["_"]*len(chosen_word)
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    index = 0
    if not guess.isalpha() or not len(guess) == 1:
        print(f"{guess} is not a letter.\nYou lose!")
        break
    if not guess in chosen_word:
        lives-=1
        print(f"Letter {guess} is not in the word. You lose a life. Lives left {lives}")
    if guess in display:
        print("You have already chosen this letter.")
    for letter in chosen_word:
        if letter == guess:
            display[index] = letter
        index+=1
    print(f"{' '.join(display)}")
    if not display.__contains__("_"):
        print("You won!")
        end_of_game = True
    if lives == 0:
        print("You lose!")
        end_of_game = True
    print(hangman_art.stages[lives])
