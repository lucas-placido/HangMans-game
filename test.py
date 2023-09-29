import pytest
import main


game = main.HangmanGame()
class TestHangmans():    
    def test_initiazeWord(self):
        assert game.initializeWord()[1] == 200
        assert len(game.initializeWord()[0]) > 0

    def test_updateWordState(self):
        word, word_state = "hello", ["_", "_", "_", "_", "_"]
        letter1, letter2 = 'e', 'l'
        assert game.updateWordState(word_state, letter1, word) == (["_", "e", "_", "_", "_"], 1)
        assert game.updateWordState(word_state, letter2, word) == (["_", "e", "l", "l", "_"], 2)

    def test_getDraw(self):
        assert game.getDraw(errors=0, manDraw=None) == [
            "  |            ",
            "  |------      ",
            "  |            ",
            "  |            ",
            "  |            ",
            "  |            ",
            "__|__          ",
            ]
        assert game.getDraw(errors=1, manDraw=game.getDraw(errors=0, manDraw=None)) == [
            "  |            ",
            "  |------      ",
            "  |     |      ",
            "  |            ",
            "  |            ",
            "  |            ",
            "__|__          ",
            ]

    def test_showDrawState(self):
        draw_state = game.getDraw(errors=0, manDraw=None)
        assert game.showDrawState(draw_state=draw_state) == 1

    def test_endGame(self):
        ifCase, elseCase = 7, 6
        word = 'hello'
        assert game.endGame(errors=ifCase, word=word) == 1
        assert game.endGame(errors=elseCase, word=word) == 0

t = TestHangmans()

t.test_initiazeWord()
t.test_updateWordState()
t.test_getDraw()
t.test_showDrawState()
t.test_endGame()
