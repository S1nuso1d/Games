#Игра угадай число
import random
from game_func import playrs_name, random_user, diapazon_game1, diapazon_game2


def menu():
    print("\nДобро пожаловать в игру угадай число")
    print("1. Играть с компьютером")
    print("2. Играть вдвоем")
    print("3. Выход")


def game_comp():
    rang1, rang2 = diapazon_game1()
    radn_nam = random.randint(rang1, rang2)
    print("Компьютер загадал число, попробуй его угадать: ")

    while True:
        user_num = 0
        while user_num == 0:
            try:
                user_num = int(input())
            except ValueError:
                print("Введите лучше число!")

        if user_num == radn_nam:
            print("Вы угадали")
            break

        else:
            print("Не угадали")


def game_two():
    username1, username2 = playrs_name()
    player1, player2 = random_user(name1=username1, name2=username2)
    print(f"{player1}, укажите диапазон и загадываемое число")
    num_player1 = diapazon_game2()

    print(f"{player2}, попытайтесь угадать число")
    while True:
        num_player2 = 0
        while num_player2 == 0:
            try:
                num_player2 = int(input())
            except ValueError:
                print("Введите лучше число!")

        if num_player1 == num_player2:
            print("Вы угадали")
            break
        else:
            print("Не угадали")


    #сделать задержку по выводу
    print("\n\nТеперь меняемся ролями")
    print(f"{player2}, укажите диапазон и загадываемое число")
    num_player2 = diapazon_game2()

    print(f"{player1}, попытайтесь угадать число")
    while True:
        num_player1 = 0
        while num_player1 == 0:
            try:
                num_player1 = int(input())
            except ValueError:
                print("Введите лучше число!")

        if num_player2 == num_player1:
            print("Вы угадали")
            break
        else:
            print("Не угадали")


def game():
    while True:
        menu()
        print("Ваш выбор: ", end="")
        choise = input()

        if choise == "3":
            break

        if choise == "1":
            game_comp()

        elif choise == "2":
            game_two()


if __name__ == "__main__":
    game()