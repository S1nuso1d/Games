class Nursery:
    def __init__(self, *,  name: str, age: int, view: str, satiety: bool, mood: bool) -> None:
        self.name = name
        self.age = age
        self.view = view #вид
        self.satiety = satiety #сытость
        self.mood = mood #настроение

    def __str__(self):
        return f"Питомец: {self.name}, возрастом: {self.age}, вид: {self.view}, сытый: {self.satiety} и его настроение: {self.mood}"


def menu() -> None:
    print("\nМеню")
    print("1. Завести питомца")
    print("2. Показать всех")
    print("3. Покормить")
    print("4. Поиграть")
    print("5. Пропустить час")
    print("6. Выход")