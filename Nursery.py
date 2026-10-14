class Pet:
    def __init__(self, *,  name: str, age: int, view: str, satiety: int = 5, mood: int = 5) -> None:
        self.name = name
        self.age = age
        self.view = view #вид
        self.satiety = satiety #сытость
        self.mood = mood #настроение

    def __str__(self):
        return f"Питомец: {self.name}, возрастом: {self.age}, вид: {self.view}, сытый: {self.satiety} и его настроение: {self.mood}"


def menu() -> None:
    print("\n\tМеню")
    print("1. Завести питомца")
    print("2. Показать всех")
    print("3. Покормить")
    print("4. Поиграть")
    print("5. Пропустить час")
    print("6. Выход")


def display_pets(pets) -> None:
    print("\nВаши питомцы")
    for number, pet in enumerate(pets, start=1):
        print(f"{number}. {pet}")

def numbers_pet() -> int:
    num = 0
    while num == 0:
        try:
            num = int(input("Введите номер питомца: "))
        except ValueError:
            print("Введите лучше число")
    return num - 1


def game() -> None:
    pets = []
    choice = 0
    while True:
        menu()
        try:
            choice = int(input("Ваш выбор: "))
        except ValueError:
            print("Введите лучше число")

        if choice == 6:
            break

        elif choice == 1:
            print("\nДавайте заведем питомца:")
            name = str(input("Введите имя животного: "))
            age = int(input("Введите возраст: "))
            view = str(input("Введите вид: "))

            pets.append(Pet(name=name, age=age, view=view))

        elif choice == 2:
            if pets:
                display_pets(pets)
            else:
                print("Питомцев пока нет")

        elif choice == 3:
            if not pets:
                print("Питомцев пока нет")
                continue

            display_pets(pets)
            num = numbers_pet()

            if num < 0 or num >= len(pets):
                print("Такого питомца нет")
                continue

            pet = pets[num]

            if pet.satiety == 10:
                print("Ваш питомец сыт")
            else:
                print(f"Кормим вашего питомца, {pet.name}")
                pet.satiety = min(10, pet.satiety + 2)
                print(f"Сытость вашего питомца: {pet.satiety}")


        elif choice == 4:
            if not pets:
                print("Питомцев пока нет")
                continue

            display_pets(pets)
            num = numbers_pet()

            if num < 0 or num >= len(pets):
                print("Такого питомца нет")
                continue

            pet = pets[num]
            print(f"Играем с вашим питомцем, {pet.name}")
            pet.mood = min(10, pet.mood + 2)
            pet.satiety = max(0, pet.satiety - 1)
            print(f"Настроение вашего питомца: {pet.mood}, сытость: {pet.satiety}")

        elif choice == 5:
            if not pets:
                print("Питомцев пока нет")
                continue
            print("Пропустить час")
            for pet in pets:
                pet.satiety = max(0, pet.satiety - 1)
                pet.mood = max(0, pet.mood - 1)
                print(f"{pet.name}: сытость {pet.satiety}, настроение {pet.mood}")
                if pet.satiety == 0:
                    print(f"{pet.name} голодный")
                if pet.mood == 0:
                    print(f"{pet.name} скучает")


if __name__ == "__main__":
    game()