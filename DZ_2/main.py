import task1
import task2
import task3


def display_menu():
    print("\nВиберіть завдання для виконання:")
    print("1. Завдання 1")
    print("2. Завдання 2")
    print("3. Завдання 3")
    print("4. Вийти")


def main():
    while True:
        display_menu()
        choice = input("Введіть номер завдання (1-4): ")

        if choice == "1":
            task1.task1()
        elif choice == "2":
            task2.task2()
        elif choice == "3":
            task3.task3()
        elif choice == "4":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
