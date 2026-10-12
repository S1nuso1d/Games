import buk
import guess_number
import quiz
import the_gallows

def menu():
    print("\nMеню")
    print("1. Угадай число")
    print("2. Квиз")
    print("3. Висельница")
    print("4. Быки и коровы")
    print("5. Выход")


def main():
    while True:
        menu()
        try:
            choice = int(input("Ваш выбор: "))
        except ValueError:
            print("Введите лучше число!")
            continue

        if choice == 5:
            break
        elif choice == 1:
            guess_number.game()
        elif choice == 2:
            quiz.game()
        elif choice == 3:
            the_gallows.game()
        elif choice == 4:
            buk.game()
        else:
            print("Введите число от 1 до 5")


if __name__ == "__main__":
    main()