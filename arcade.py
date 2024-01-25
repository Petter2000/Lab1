from hangman import *
from highscore import *
from utils import clear_console

try:
    clear_console()
    while(True):
        print("\nVälkommen till \033[33mArkadmaskinen\033[0m\n")
        print("[\033[33mH\033[0m] Hänga gubbe")
        print("[\033[33mV\033[0m] Visa topplistan")
        print("[\033[91mR\033[0m] Rensa topplistan")
        print("För att avsluta tryck [\033[31m1\033[0m]\n")
        option = input("\nVälj spel: ")
        clear_console()

        if (option == '1'):
            print("\nAvslutar Arkadmaskinen\n")
            exit()
        elif (option.lower() == 'h'):
            set_running_game_to_true()
            play_hangman()
        elif(option.lower() == 'v'):
            print_highscore_list()
        elif(option.lower() == 'r'):
            clear_highscore_list()
        else:
            print("Ogiltig input")
except Exception as e:
    print(f"Något gick fel: {e}. Kanske lika bra. Läs en bok istället")
