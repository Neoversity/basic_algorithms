import task1
import task2
import task3
import task4

def main():
    while True:
        print("Оберіть завдання:")
        print("1: Знайти найбільше значення у дереві")
        print("2: Знайти найменше значення у дереві")
        print("3: Знайти суму всіх значень у дереві")
        print("4: Ієрархічна структура коментарів")
        print("5: Вихід")
        
        choice = input("Введіть номер завдання: ")

        if choice == '1':
            task1_main()
        elif choice == '2':
            task2_main()
        elif choice == '3':
            task3_main()
        elif choice == '4':
            task4_main()
        elif choice == '5':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

def task1_main():
    # Створюємо нове дерево
    bst = task1.BinarySearchTree()
    
    # Вставляємо ключі в дерево
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    
    # Знаходимо та виводимо найбільше значення у дереві
    print("Найбільше значення у дереві:", task1.find_max_value(bst.root))
    
    # Візуалізуємо дерево
    task1.visualize_tree(bst.root)

def task2_main():
    # Створюємо нове дерево
    bst = task2.BinarySearchTree()
    
    # Вставляємо ключі в дерево
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    
    # Знаходимо та виводимо найменше значення у дереві
    print("Найменше значення у дереві:", task2.find_min_value(bst.root))
    
    # Візуалізуємо дерево
    task2.visualize_tree(bst.root)

def task3_main():
    # Створюємо нове дерево
    bst = task3.BinarySearchTree()
    
    # Вставляємо ключі в дерево
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    
    # Знаходимо та виводимо суму всіх значень у дереві
    print("Сума всіх значень у дереві:", task3.sum_of_values(bst.root))
    
    # Візуалізуємо дерево
    task3.visualize_tree(bst.root)

def task4_main():
    # Створюємо основний коментар
    root_comment = task4.Comment("Яка чудова книга!", "Бодя")
    
    # Створюємо відповіді до основного коментаря
    reply1 = task4.Comment("Книга повне розчарування :(", "Андрій")
    reply2 = task4.Comment("Що в ній чудового?", "Марина")
    
    # Додаємо відповіді до основного коментаря
    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)
    
    # Створюємо відповідь до першого коментаря
    reply1_1 = task4.Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)

    # Видаляємо перший коментар
    reply1.remove_reply()
    
    # Відображаємо коментарі
    root_comment.display()

if __name__ == "__main__":
    main()
