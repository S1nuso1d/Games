import random

def playrs_name() -> tuple[str, str]:
    try:
        user_name1 = str(input("\nВведите имя игрока 1: "))
        user_name2 = str(input("Введите имя игрока 2: "))
    except ValueError:
        print("Введите имя корректно!")
    return user_name1, user_name2


def random_user(*, name1="User1", name2="User2") -> tuple[str, str]:
    players = [name1, name2]
    random.shuffle(players)
    print(f"Первым будет {players[0]}")
    print(f"{players[1]}, ты будешь вторым")
    return players[0], players[1]


def diapazon_game1() -> int:
    rang1 = 0
    rang2 = 0
    while rang1 >= rang2 or rang2 > 99:
        try:
            rang1 = int(input("Введите диапазон от(0-99):  "))
            rang2 = int(input("Введите диапазон до(0-99):  "))
        except ValueError:
            print("Введите лучше число!")
    return rang1, rang2

def diapazon_game2() -> int:
    rang1, rang2 = diapazon_game1()
    print(f"Диапазон {rang1}, {rang2}")
    num = 0
    while num == 0:
        try:
            num = int(input("Введите число: "))
        except ValueError:
            print("Введите лучше число!")
    return num

