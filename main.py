from draw import getDrawState, showDrawState
from word import initWordState, initializeWord, updateWordState
import time

class HangMan():
    def __init__(self, errors=6) -> None:        
        self.errors = errors

    def initialize_game(self):
        word = initializeWord()                    
        word_state = initWordState(word)
        errors = 0        
        inputs = []
        
        print("Welcome to HangMan's game !!\n")
        draw_state = getDrawState(errors)
        showDrawState(draw_state)
        print("\n", word_state, "\n")
        while (errors < self.errors) and ('_' in word_state):            
            # Test user input
            print("write 'try' to try the full word")
            userInput = input("Type a letter: ")
            if userInput == 'try':
                inputWord = input("Type the whole word: ")
                if inputWord.lower() == word:
                    draw_state = getDrawState(errors)
                    showDrawState(draw_state)
                    word_state = [i for i in word]
                    word_state = ' '.join(word_state)
                    print("\n", word_state, "\n")            
                    break
                else:
                    draw_state = getDrawState(errors)
                    showDrawState(draw_state)
                    print("\n", word_state, "\n")
                    errors = self.errors
                    break
            else:
                letter = userInput
            if len(letter) != 1 or not letter.isalpha():
                print("Insert a valid letter")
                print("-----------------------------------\n")
                continue
            
            if letter not in inputs:
                inputs.append(letter)
            else:
                print(f"The letter '{letter}' was already picked")
                print("Choose another one !!\n")
                continue

            # Checks if letter is in the word and update the wordState or the drawState
            if letter.lower() in word:
                word_state, times = updateWordState(word_state, letter, word)
                triesNumber = self.errors - errors
                print(f"There is {times} '{letter}' in the word :)")
                print(f"You have {triesNumber} tries")
                print("-----------------------------------\n")
            else:
                errors += 1
                triesNumber = self.errors - errors
                print(f"There is no '{letter}' in the word :(")
                print(f"You have {triesNumber} tries")
                print("-----------------------------------\n")
            
            print(f"\nUsed Letters: {' '.join(inputs)}")
            draw_state = getDrawState(errors)
            showDrawState(draw_state)
            print("\n", word_state, "\n")            

        if errors == self.errors:                    
            print("You loose the game !!")
            print(f"The word was '{word}'\n")
            print("Play again")
        else:
            print("Congratulations !!")
            print("You won the game :)")
        
        time.sleep(30)

game = HangMan()
if __name__ == "__main__":
    game.initialize_game()