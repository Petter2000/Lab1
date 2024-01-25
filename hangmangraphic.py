def hang_row_1(score):
    if (score > 8 ):
        return "               "
    else:
        return "      _______  "

def hang_row_2(score):
    if (score > 9):
        return "               "
    elif (score > 7):
        return "     |         "
    elif (score > 6):
        return "     |/        "
    else:
        return "     |/     |  "

def hang_row_3(score):
    if (score > 9):
        return "               "
    elif (score > 5):
        return "     |         "
    else:
        return "     |      O  "

def hang_row_4(score):
    if (score > 9):
        return "               "
    elif (score > 4):
        return "     |         "
    elif (score > 3):
        return "     |      |  "
    elif (score > 2):
        return "     |     /|  "
    else:
        return "     |     /|\ "

def hang_row_5(score):
    if (score > 9):
        return "               "
    elif (score > 1):
        return "     |         "
    elif (score > 0):
        return "     |     /   "
    else:
        return "     |     / \ "

def hang_row_6(score):
    if (score == 10):
        return "_______________"
    else:
        return "_____|_________"
