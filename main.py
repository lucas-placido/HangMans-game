import time
import requests

class HangmanGame():
    def __init__(self, errors=7) -> None:        
        self.errors = errors
    
    def initializeWord(self):
        url = "https://random-word-api.herokuapp.com/word?number=1"
        response = requests.get(url)
        return response.json()[0], response.status_code
    
    def updateWordState(self, word_state, letter, word):    
        times = 0
        for i, x in enumerate(word):
            if x == letter:
                word_state[i] = letter
                times += 1
        return word_state, times
    
    def getDraw(self, errors, manDraw = None):
        if not manDraw:
            manDraw = [
            "  |            ",
            "  |------      ",
            "  |            ",
            "  |            ",
            "  |            ",
            "  |            ",
            "__|__          ",
            ]
        else:
            if errors == 1:
                manDraw[2] = r"  |     |      "
            if errors == 2:
                manDraw[3] = r"  |     O      "
            if errors == 3:
                manDraw[4] = r"  |     |      "
            if errors == 4:
                manDraw[4] = r"  |    /|      "
            if errors == 5:
                manDraw[4] = r"  |    /|\     "
            if errors == 6:
                manDraw[5] = r"  |    /       "
            if errors == 7:
                manDraw[5] = r"  |    / \     "
        return manDraw

    def showDrawState(self, draw_state):
        for row in draw_state:
            print(row)
        return 1
    
    def showGameState(self, errors, word_state, manDraw):
        draw_state = self.getDraw(errors, manDraw)
        self.showDrawState(draw_state)
        print("\n", ' '.join(word_state), "\n")
        return draw_state

    def endGame(self, errors, word):
        if errors == self.errors:
            print("You lose the game !!")
            print(f"The word was '{word}'\n")
            print("Play again")
            return 1
        else:
            print("Congratulations !!")
            print("You won the game :)")
            return 0
    
    def initialize_game(self):
        word, _ = self.initializeWord()                    
        word_state = ["_"] * len(word)
        errors = 0        
        inputs = []
        
        print("Welcome to HangMan's game !!\n")        
        print("""
**How to play**
    1. Enter a letter per time
    2. Write 'try' anytime to try the full word (you will loose if it's not correct)
    3. Have fun :D
        """)
        drawState = self.showGameState(errors, word_state, None)
                
        while (errors < self.errors) and ('_' in word_state):            
            # Test user input            
            userInput = input("Type a letter: ").lower()
            if userInput == 'try':
                inputWord = input("Type the whole word: ")
                if inputWord == word:
                    drawState = self.showGameState(errors, word_state, drawState)
                    break
                else:
                    drawState = self.showGameState(errors, word_state, drawState)
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
            if letter in word:
                word_state, times = self.updateWordState(word_state, letter, word)
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
            
            print(f"Used Letters: {' '.join(inputs)}")
            drawState = self.showGameState(errors, word_state, drawState)

        
        self.endGame(errors, word)
        
        time.sleep(15)

game = HangmanGame()
if __name__ == "__main__":
    game.initialize_game()