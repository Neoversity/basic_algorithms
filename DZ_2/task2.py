# Завдання 2

# Необхідно розробити функцію, яка приймає рядок як вхідний параметр,
# додає всі його символи до двосторонньої черги (deque з модуля collections в Python),
# а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом.
# Програма повинна правильно враховувати як рядки з парною,
# так і з непарною кількістю символів, а також бути нечутливою до регістру та пробілів.


from collections import deque


def is_palindrome(s):
    # Приводимо рядок до нижнього регістру та видаляємо пробіли
    s = "".join(s.lower().split())

    # Створюємо двосторонню чергу
    d = deque(s)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False

    return True


def task2():
    # Приклади використання
    print(is_palindrome("A man a plan a canal Panama"))  # True
    print(is_palindrome("Hello World"))  # False
    print(is_palindrome("racecar"))  # True
    print(is_palindrome("No lemon no melon"))  # True


if __name__ == "__main__":
    task2()
