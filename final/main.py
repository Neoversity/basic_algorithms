from tasks import task_1, task_2, task_3, task_4, task_5

def main():
    """
    Основний цикл програми, який дозволяє користувачеві вибирати завдання для виконання.
    """
    while True:
        print("Select a task to execute:")
        print("1. Linked List Operations")
        print("2. Pythagoras Tree Fractal")
        print("3. Dijkstra's Algorithm")
        print("4. Visualize Binary Heap")
        print("5. Visualize Tree Traversal")
        print("6. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            task_1()
        elif choice == '2':
            task_2()
        elif choice == '3':
            task_3()
        elif choice == '4':
            task_4()
        elif choice == '5':
            task_5()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
