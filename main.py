import time

import requests


class HangmanGame:
    def __init__(self, errors=7, closingTime=5) -> None:
        self.errors = errors
        self.closingTime = closingTime

    def initialize_word(self):
        """
        Inicialize the word by choosing a random word from the Random Word API.
        Returns:

            Word (str)
            status_code (int)
        """

        url = 'https://random-word-api.herokuapp.com/word?number=1'
        response = requests.get(url, timeout=5)
        return response.json()[0], response.status_code

    def update_word_state(self, word_state, letter, word):
        times = 0
        for i, x in enumerate(word):
            if x == letter:
                word_state[i] = letter
                times += 1
        return word_state, times

    def get_draw(self, errors, manDraw=None):
        if not manDraw:
            manDraw = [
                '  |            ',
                '  |------      ',
                '  |            ',
                '  |            ',
                '  |            ',
                '  |            ',
                '__|__          ',
            ]
        else:
            if errors == 1:
                manDraw[2] = r'  |     |      '
            if errors == 2:
                manDraw[3] = r'  |     O      '
            if errors == 3:
                manDraw[4] = r'  |     |      '
            if errors == 4:
                manDraw[4] = r'  |    /|      '
            if errors == 5:
                manDraw[4] = r'  |    /|\     '
            if errors == 6:
                manDraw[5] = r'  |    /       '
            if errors == 7:
                manDraw[5] = r'  |    / \     '
        return manDraw

    def show_draw_state(self, draw_state):
        for row in draw_state:
            print(row)
        return 1

    def show_game_state(self, errors, word_state, manDraw):
        draw_state = self.get_draw(errors, manDraw)
        self.show_draw_state(draw_state)
        print('\n', ' '.join(word_state), '\n')
        return draw_state

    def end_game(self, errors, word):
        if errors == self.errors:
            print('You lose the game !!')
            print(f"The word was '{word}'\n")
            return 1
        print('Congratulations !!')
        print('You won the game :)')
        return 0

    def ask_play_again(self):
        try:
            user_input = input('Play again? (Y/N): ').lower()
        except AttributeError:
            print('Enter a valid response (Y/N)')
            self.ask_play_again()
        return user_input

    def play_again(self, user_input):
        if user_input == 'y':
            game.initialize_game()
        elif user_input == 'n':
            print('Until next time :D')
            print(f'Closing in {self.closingTime}')
            time.sleep(self.closingTime)
        else:
            print('Insert a valid character (Y/N)')
            print('------------------------------\n')
            response = self.ask_play_again()
            self.play_again(response)

    def initialize_game(self):
        word, _ = self.initialize_word()
        word_state = ['_'] * len(word)
        errors = 0
        inputs = []

        print("Welcome to HangMan's game !!\n")
        print(
            """
**How to play**
    1. Enter a letter per time
    2. Write 'try' anytime to try the full word (you will loose if it's not correct)
    3. Have fun :D
        """
        )
        drawState = self.show_game_state(errors, word_state, None)

        while (errors < self.errors) and ('_' in word_state):
            # Test user input
            userInput = input('Type a letter: ').lower()
            if userInput == 'try':
                inputWord = input('Type the whole word: ')
                if inputWord == word:
                    drawState = self.show_game_state(
                        errors, word_state, drawState
                )
                    break
                
                
                drawState = self.show_game_state(
                errors, word_state, drawState
                )
                errors = self.errors
                break

            letter = userInput
            if len(letter) != 1 or not letter.isalpha():
                print('Insert a valid letter')
                print('-----------------------------------\n')
                continue

            if letter not in inputs:
                inputs.append(letter)
            else:
                print(f"The letter '{letter}' was already picked")
                print('Choose another one !!\n')
                continue

            # Checks if letter is in the word and update the wordState or the drawState
            if letter in word:
                word_state, times = self.update_word_state(
                    word_state, letter, word
                )
                triesNumber = self.errors - errors
                print(f"There is {times} '{letter}' in the word :)")
                print(f'You have {triesNumber} tries')
                print('-----------------------------------\n')
            else:
                errors += 1
                triesNumber = self.errors - errors
                print(f"There is no '{letter}' in the word :(")
                print(f'You have {triesNumber} tries')
                print('-----------------------------------\n')

            print(f"Used Letters: {' '.join(inputs)}")
            drawState = self.show_game_state(errors, word_state, drawState)

        self.end_game(errors, word)

        response = self.ask_play_again()
        self.play_again(response)


game = HangmanGame()
if __name__ == '__main__':
    game.initialize_game()
