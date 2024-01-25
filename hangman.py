from utils import clear_console
import random
from hangmangraphic import *
from highscore import update_highscore_list
# Hangman

class GameInfo:
        def __init__(self, secret_word):
            self.secret_word = secret_word
            self.board = "_" * len(secret_word)
            self.number_of_guesses = 0
            self.guessed_letters = ""
            self.score = 10

list_of_words = ["ko", "mus", "apa", "katt", "gris", "zebra", "lejon", "tiger",
                 "struts","giraff", "krokodil","noshörning", "fladdermus"]

def play_hangman():
    while(running_game):
        set_running_rounds_to_true()
        print("\nVälkommen till \033[93mHänga gubbe!\033[0m")
        game_info = set_up_game_info()

        while(running_rounds):
            print_round_result(game_info)
            player_guessing(game_info)
            update_board(game_info)
            check_game_condition(game_info)

def set_up_game_info():
    game_info = GameInfo(chose_secret_word())
    return game_info

def chose_secret_word():
    rnd_num = random.randint(0, len(list_of_words) -1)
    return list_of_words[rnd_num]

def player_guessing(game_info):
    guess = input("\n\nGissa på en bokstav:")
    guess.lower()
    clear_console()
    handle_guess(guess, game_info)

def update_board(game_info):
    board = ""
    for char in game_info.secret_word:
        if (char in game_info.guessed_letters):
            board += char
        else:
            board +="_"
    game_info.board = board

def handle_guess(guess, game_info):
    is_valid = check_if_valid_guess(guess, game_info)
    if (is_valid):
        game_info.guessed_letters += guess
        game_info.number_of_guesses += 1
        print(f"Resultat för runda {game_info.number_of_guesses}: ", end='')
        if (guess in game_info.secret_word):
            print(f"'\033[93m{guess}\033[0m' fanns med på \033[93m{game_info.secret_word.count(guess)}\033[0m {'ställen' if game_info.secret_word.count(guess) > 1 else 'ställe'}")
        else:
            print(f"'\033[93m{guess}\033[0m' finns inte med i det hemlig ordet.")
            game_info.score -= 1

def check_if_game_is_won(game_info):
    if (game_info.board == game_info.secret_word):
        print_winning_result(game_info)

def check_if_game_is_lost(game_info):
    if(game_info.score == 0):
        print_losing_result(game_info)

def check_game_condition(game_info):
    check_if_game_is_won(game_info)
    check_if_game_is_lost(game_info)

def check_if_valid_guess(guess, game_info):
    if(guess == '1'):
        print("\nAvslutar spelet.")
        set_running_rounds_to_false()
        set_running_game_to_false()
        return False
    if (guess in game_info.guessed_letters):
        print(f"Du har redan gissat på '\033[33m{guess}\033[0m'")
        return False
    if not (len(guess) == 1 and guess.isalpha()):
        print("Ogiltig gissning. Gissa endast på 1 bokstav åt gången.")
        return False
    return True

def print_round_result(game_info):
    print(f"{hang_row_1(game_info.score)}")
    print(f"{hang_row_2(game_info.score)} [Runda {game_info.number_of_guesses +1}]")
    print(f"{hang_row_3(game_info.score)} Ordets längd: \033[33m{len(game_info.secret_word)}\033[0m bokstäver")
    print(f"{hang_row_4(game_info.score)} {guessed_letters(game_info)}")
    print(f"{hang_row_5(game_info.score)} {score(game_info)}")
    print(f"{hang_row_6(game_info.score)} För att avsluta tryck [\033[31m1\033[0m]\n")
    print("Spelplan: ", end='')
    for char in game_info.board:
        print(f"\033[33m{char}\033[0m", end=' ')

def print_winning_result(game_info):
    print(f"{hang_row_1(game_info.score)}")
    print(f"{hang_row_2(game_info.score)}  Game Over! \033[92mDu Vann!\033[0m")
    game_over_results(game_info)
    update_highscore_list(game_info)
    play_again()

def print_losing_result(game_info):
    print(f"{hang_row_1(game_info.score)}")
    print(f"{hang_row_2(game_info.score)}  Game Over! \033[91mDu förlorade!\033[0m")
    game_over_results(game_info)
    play_again()

def game_over_results(game_info):
    print(f"{hang_row_3(game_info.score)}  {secret_word(game_info)}")
    print(f"{hang_row_4(game_info.score)}  {guessed_letters(game_info)}")
    print(f"{hang_row_5(game_info.score)}  {number_of_guesses(game_info)}")
    print(f"{hang_row_6(game_info.score)}  {score(game_info)}\n\n")

def guessed_letters(game_info):
    return f"Gissade bokstäver: {', '.join(game_info.guessed_letters) if game_info.guessed_letters else 'Inga'}"

def score(game_info):
    return f"Poäng: \033[33m{game_info.score}\033[m"

def number_of_guesses(game_info):
    return f"Antal gissningar: {game_info.number_of_guesses}"

def secret_word(game_info):
    return f"Det hemliga ordet var '\033[33m{game_info.secret_word}\033[0m'"

def play_again():
    player_deciding = True
    while(player_deciding):
        option = input("Spela igen? (J)a / (N)ej: ")
        if(option.lower() == 'j' ):
            set_running_rounds_to_false()
            player_deciding = False
        elif(option.lower() == 'n'):
            set_running_rounds_to_false()
            set_running_game_to_false()
            player_deciding = False
        else:
            print("Ogiltig input")
    clear_console()

def set_running_game_to_true():
    global running_game
    running_game = True

def set_running_rounds_to_true():
    global running_rounds
    running_rounds = True

def set_running_rounds_to_false():
    global running_rounds
    running_rounds = False

def set_running_game_to_false():
    global running_game
    running_game = False
