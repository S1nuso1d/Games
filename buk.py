from game_func import *
import random

def menu() -> None:
    print("\nМеню")
    print("1. Играть с компьютером")
    print("2. Играть вдвоем")
    print("3. Правила")
    print("4. Выход")

def play_computer() -> None:
    computer_choice = []

    for i in range(4):
        computer_choice.append(random.randint(1, 10))

    players_num = []

    for i in range(4):
        players_num.append(int(input("Введите ваши цифры по одной: ")))

    print(players_num)

    used_computer = [False, False, False, False]
    used_player = [False, False, False, False]
    for i in range(4):
        if players_num[i] == computer_choice[i]:
            used_computer[i] = True
            used_player[i] = True
            print(players_num[i], "на своём месте")

    for a in range(4):
        if used_player[a]:
            continue
        for i in range(4):
            if used_computer[i]:
                continue
            if players_num[a] == computer_choice[i]:
                used_computer[i] = True
                print(players_num[a], "есть, но стоит не на своём месте")
                break

user_name1 = ""
user_name2 = ""

players1 = ""
players2 = ""

list_players1 = []
list_players2 = []

menu()
while True:
    choice = int(input("Ваш выбор: "))
    if choice == 4:
        break

    elif choice == 1:
        play_computer()

    elif choice == 2:
        user_name1, user_name2 = playrs_name()
        players1, players2 = random_user(name1= user_name1, name2= user_name2)
        for i in range(4):
            list_players1.append(int(input(f"{players1} Введите ваши цифры по одной: ")))