from utils import clear_console, remove_file

def update_highscore_list(game_info):
    name = get_player_name()
    with open('highscore_list.txt', 'a') as file:
         file.write(f"{name} {game_info.score} {len(game_info.secret_word)}\n")

def print_highscore_list():
    try:
        clear_console()
        with open('highscore_list.txt', 'r') as file:
            highscore_list = [line.strip().split() for line in file]
            highscore_list.sort(key=lambda x: (int(x[1]), int(x[2])), reverse=True)
            print("[Namn]     [Poäng]     [Ordets längd]\n")
            for entry in highscore_list:
                name, score, word_length = entry
                print(f"{name}{' ' * (12 -len(name))}{score}{' ' * (11 - len(str(score)))} {(word_length)}")

            input("\nTryck för att fortsätta")
    except FileNotFoundError:
        print("Topplistan är tom")

def get_player_name():
    writing_name = True
    while(writing_name):
        name = input("Skriv ditt namn: ")
        if(len(name) > 10):
            print("Namnet är för långt. Max 10 tecken.")
        elif(name == ''):
            name = "namnlös"
            writing_name = False
        else:
            writing_name = False
    return name

def clear_highscore_list():
    try:
        remove_file('highscore_list.txt')
        print("Topplistan rensad!")
    except FileNotFoundError:
        print("Topplistan är tom")