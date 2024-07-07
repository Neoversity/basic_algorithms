# Завдання 1
# Потрібно розробити програму, яка імітує приймання й обробку заявок:
# програма має автоматично генерувати нові заявки
# (ідентифіковані унікальним номером або іншими даними), додавати їх до черги,
# а потім послідовно видаляти з черги для "обробки",
# імітуючи таким чином роботу сервісного центру.


# Ось псевдокод для завдання з використанням черги
# У цьому псевдокоді використовуються дві основні функції:
# generate_request(), яка генерує нові заявки та додає їх до черги,
# та process_request(), яка обробляє заявки, видаляючи їх із черги.
# Головний цикл програми виконує ці функції,
# імітуючи постійний потік нових заявок та їх обробку.

import queue

# Створюємо чергу

request_queue = queue.Queue()

# Лічиьник запитів
request_id_counter = 1


def generate_request():
    global request_id_counter
    request_id = f"Request-{request_id_counter}"
    request_queue.put(request_id)
    print(f"Generated: {request_id}")
    request_id_counter += 1


def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Processing: {request_id}")
    else:
        print("Queue is empty. No requests to process.")


def task1():
    while True:
        user_input = input(
            "Enter 'g' to generate a request, 'p' to process a request, or 'q' to quit: "
        )
        if user_input.lower() == "g":
            generate_request()
        elif user_input.lower() == "p":
            process_request()
        elif user_input.lower() == "q":
            print("Exiting program.")
            break
        else:
            print("Invalid input. Please enter 'g', 'p', or 'q'.")


if __name__ == "__main__":
    task1()
