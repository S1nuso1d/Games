import random
import tkinter as tk
from tkinter import simpledialog


def clear_screen():
    print("\033[2J\033[H", end="", flush=True)


def menu():
    print("Начнем играть?")
    print("1.Начать игру")
    print("2.Выход")


print("\tПривет")
print("Это игра висельница")
print("В ней один игрок загадывает слово, а второй пытается его угадать, при этом у него есть 3 попытки ошибиться")

user_name1 = ""
user_name2 = ""

while True:
    menu()
    choice = input("Ваш выбор: ")

    if choice == "2":
        break

    if choice == "1":
        clear_screen()

        if user_name1 == "":
            user_name1 = input("Давайте познакомимся и начнем игру. Начнем с игрока 1, как вас зовут?: ")
            user_name2 = input("Игрок 2, как вас зовут?: ")
            print("")

        players = [user_name1, user_name2]
        guesser = random.choice(players)

        guesser_index = players.index(guesser)
        guess_index = 1 - guesser_index
        guess_name = players[guess_index]

        print(f"Загадывать слово будет {guesser}")
        print(f"{guess_name}, ты угадываешь!")

        print("\n\tНачнем игру")
        print("Введите слово в отдельное окно")

        root = tk.Tk()
        root.withdraw()
        word = simpledialog.askstring("Загадать слово", f"Введите слово, {guesser}:")
        root.destroy()
        if not word:
            clear_screen()
            continue

        shown = ["-"] * len(word)
        print("".join(shown))

        lives = 3

        while lives > 0 and "-" in shown:
            attempt = input("Попробуйте угадать букву: ")
            if attempt in word:
                for i in range(len(word)):
                    if word[i] == attempt:
                        shown[i] = attempt
            else:
                lives -= 1
                print(f"Неверно. Осталось попыток: {lives}")
            print("".join(shown))

        if lives == 0:
            print("Жизней не осталось")
            print(f"Слово было: {word}")
        else:
            print("Вы угадали слово")

        input("Нажмите Enter, чтобы вернуться в меню")
        clear_screen()
