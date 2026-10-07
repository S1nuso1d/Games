import random
import tkinter as tk
from tkinter import simpledialog
from game_func import playrs_name, random_user

def menu():
    print("\nMеню")
    print("1.Начать игру")
    print("2.Выход")


def game():
    print("\tПривет")
    print("Это игра висельница")
    print("В ней один игрок загадывает слово, а второй пытается его угадать, при этом у него есть 3 попытки ошибиться")

    while True:
        menu()
        choice = input("Ваш выбор: ")

        if choice == "2":
            break

        if choice == "1":
            user_name1, user_name2 = playrs_name()
            player1, player2 = random_user(name1=user_name1, name2=user_name2)

            print(f"Загадывать слово будет {player1}")
            print(f"{player2}, ты угадываешь!")

            print("\n\tНачнем игру")
            print("Введите слово в отдельное окно")

            root = tk.Tk()
            root.withdraw()
            word = simpledialog.askstring("Загадать слово", f"Введите слово, {player1}:")
            root.destroy()
            if not word:
                continue

            shown = ["-"] * len(word)
            print("".join(shown))

            lives = 3

            while lives > 0 and "-" in shown:
                attempt = str(input("Попробуйте угадать букву: "))
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


if __name__ == "__main__":
    game()
