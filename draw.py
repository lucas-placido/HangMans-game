def draw6():
    boneco = [
    "  |            ",
    "  |------      ",
    "  |     |      ",
    "  |     O      ",
    "  |    /|\     ",
    "  |    / \     ",
    "__|__          ",
    ]
    return boneco

def draw5():
    boneco = [
    "  |            ",
    "  |------      ",
    "  |     |      ",
    "  |     O      ",
    "  |    /|\     ",
    "  |    /       ",
    "__|__          ",
    ]
    return boneco

def draw4():
    boneco = [
    "  |            ",
    "  |------      ",
    "  |     |      ",
    "  |     O      ",
    "  |    /|\     ",
    "  |            ",
    "__|__          ",
    ]
    return boneco

def draw3():
    boneco = [
    "  |            ",
    "  |------      ",
    "  |     |      ",
    "  |     O      ",
    "  |    /|      ",
    "  |            ",
    "__|__          ",
    ]
    return boneco

def draw2():
    boneco = [
    "  |            ",
    "  |------      ",
    "  |     |      ",
    "  |     O      ",
    "  |     |      ",
    "  |            ",
    "__|__          ",
    ]
    return boneco

def draw1():
    boneco = [
    "  |            ",
    "  |------      ",
    "  |     |      ",
    "  |     O      ",
    "  |            ",
    "  |            ",
    "__|__          ",
    ]
    return boneco

def draw0():
    boneco = [
    "  |            ",
    "  |------      ",
    "  |     |      ",
    "  |            ",
    "  |            ",
    "  |            ",
    "__|__          ",
    ]
    return boneco

def getDrawState(drawNumber):
    if drawNumber == 0:
        return draw0()
    elif drawNumber == 1:
        return draw1()
    elif drawNumber == 2:
        return draw2()
    elif drawNumber == 3:
        return draw3()
    elif drawNumber == 4:
        return draw4()
    elif drawNumber == 5:
        return draw5()
    else:
        return draw6()

def showDrawState(draw_state):
    for row in draw_state:
        print(row)
    return 