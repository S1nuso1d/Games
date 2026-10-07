import guess_number
import quiz
import the_gallows

def menu():
    print("\nMеню")
    print("1. Угадай число")
    print("2. Квиз")
    print("3. Висельница")
    print("4. Выход")


def main():
    while True:
        menu()
        try:
            choice = int(input("Ваш выбор: "))
        except ValueError:
            print("Введите лучше число!")
            continue

        if choice == 4:
            break
        elif choice == 1:
            guess_number.game()
        elif choice == 2:
            quiz.game()
        elif choice == 3:
            the_gallows.game()
        else:
            print("Введите число от 1 до 4")


if __name__ == "__main__":
    main()