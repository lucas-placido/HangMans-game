import requests 

def initializeWord():
    url = "https://random-word-api.herokuapp.com/word?number=1"
    response = requests.get(url)
    return response.json()[0]

def initWordState(word):
    underscores = "_ " * len(word)
    return underscores

def updateWordState(word_state, letter, word):
    word = [x for x in word]
    word_stateList = word_state.split(' ')
    times = 0
    for i, x in enumerate(word):
        if x == letter:
            word_stateList[i] = letter
            times += 1
    new_word_state = ' '.join(word_stateList)
    return new_word_state, times
