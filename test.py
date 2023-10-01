import main

game = main.HangmanGame()


class TestHangmans:
    def test_initiazeWord(self):
        assert game.initialize_word()[1] == 200
        assert len(game.initialize_word()[0]) > 0

    def test_update_word_state(self):
        word, word_state = "hello", ["_", "_", "_", "_", "_"]
        letter1, letter2 = "e", "l"
        assert game.update_word_state(word_state, letter1, word) == (
            ["_", "e", "_", "_", "_"],
            1,
        )
        assert game.update_word_state(word_state, letter2, word) == (
            ["_", "e", "l", "l", "_"],
            2,
        )

    def test_get_draw(self):
        assert game.get_draw(errors=0, manDraw=None) == [
            "  |            ",
            "  |------      ",
            "  |            ",
            "  |            ",
            "  |            ",
            "  |            ",
            "__|__          ",
        ]
        assert game.get_draw(errors=1, manDraw=game.get_draw(errors=0, manDraw=None)) == [
            "  |            ",
            "  |------      ",
            "  |     |      ",
            "  |            ",
            "  |            ",
            "  |            ",
            "__|__          ",
        ]

    def test_show_draw_state(self):
        draw_state = game.get_draw(errors=0, manDraw=None)
        assert game.show_draw_state(draw_state=draw_state) == 1

    def test_end_game(self):
        ifCase, elseCase = 7, 6
        word = "hello"
        assert game.end_game(errors=ifCase, word=word) == 1
        assert game.end_game(errors=elseCase, word=word) == 0

    def test_ask_play_again(self):
        pass

    def test_play_again(self):
        pass


t = TestHangmans()

t.test_initiazeWord()
t.test_update_word_state()
t.test_get_draw()
t.test_show_draw_state()
t.test_end_game()
t.test_ask_play_again()
t.test_play_again()
