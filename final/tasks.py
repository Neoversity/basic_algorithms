from linked_list import create_node, append, print_list, reverse, insertion_sort, merge_sorted_lists
from pythagoras_tree import draw_tree as draw_pythagoras_tree
from dijkstra_gui import generate_connected_random_graph
from dijkstra_visualization import visualize_graph
from dijkstra_gui import Graph, dijkstra
from heap_visualization import array_to_heap, draw_heap_tree
from tree_traversal_visualization import visualize_dfs, visualize_bfs
from food_selection import greedy_algorithm, dynamic_programming
from monte_carlo_dice import run_monte_carlo_simulation

def task_1():
    """
    Виконує завдання 1: робота з однозв'язним списком.
    """
    # Створення та виведення списку
    head = None
    head = append(head, 3)
    head = append(head, 1)
    head = append(head, 4)
    head = append(head, 2)
    print("Original list:")
    print_list(head)

    # Реверсування списку
    head = reverse(head)
    print("Reversed list:")
    print_list(head)

    # Сортування списку
    head = insertion_sort(head)
    print("Sorted list:")
    print_list(head)

    # Об'єднання двох відсортованих списків
    list1 = None
    list1 = append(list1, 1)
    list1 = append(list1, 3)
    list1 = append(list1, 5)

    list2 = None
    list2 = append(list2, 2)
    list2 = append(list2, 4)
    list2 = append(list2, 6)

    print("First sorted list:")
    print_list(list1)
    print("Second sorted list:")
    print_list(list2)

    # Об'єднання списків
    merged_head = merge_sorted_lists(list1, list2)
    print("Merged sorted list:")
    print_list(merged_head)

def task_2():
    """
    Виконує завдання 2: малювання фрактала "дерево Піфагора".
    """
    level = int(input("Enter the recursion level for the Pythagoras tree: "))
    draw_pythagoras_tree(level)

def task_3():
    """
    Виконує завдання 3: алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі.
    """
    while True:
        print("Select input method for the graph:")
        print("1. Random graph")
        print("2. Manual input")
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            num_nodes = int(input("Enter the number of nodes: "))
            num_edges = int(input("Enter the number of edges: "))
            graph = generate_connected_random_graph(num_nodes, num_edges)
            break
        elif choice == '2':
            graph = Graph()
            num_edges = int(input("Enter the number of edges: "))
            for _ in range(num_edges):
                from_node = input("Enter the start node: ")
                to_node = input("Enter the end node: ")
                weight = float(input("Enter the weight of the edge: "))
                graph.add_edge(from_node, to_node, weight)
            break
        else:
            print("Invalid choice. Please try again.")

    start_node = input("Enter the start node for Dijkstra's algorithm: ")
    shortest_paths = dijkstra(graph, start_node)

    print("Shortest paths from node {}: ".format(start_node))
    for node, distance in shortest_paths.items():
        print("Distance to {}: {:.2f}".format(node, distance))

    visualize_graph(graph, shortest_paths, start_node)

def task_4():
    """
    Виконує завдання 4: візуалізація бінарної купи.
    """
    heap_array = [int(x) for x in input("Enter the elements of the heap (space-separated): ").split()]
    heap_root = array_to_heap(heap_array)
    draw_heap_tree(heap_root)

def task_5():
    """
    Виконує завдання 5: візуалізація обходу бінарного дерева.
    """
    heap_array = [int(x) for x in input("Enter the elements of the tree (space-separated): ").split()]
    heap_root = array_to_heap(heap_array)
    
    print("Select traversal method:")
    print("1. Depth-First Search (DFS)")
    print("2. Breadth-First Search (BFS)")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        visualize_dfs(heap_root)
    elif choice == '2':
        visualize_bfs(heap_root)
    else:
        print("Invalid choice. Please try again.")

def task_6():
    """
    Виконує завдання 6: жадібний алгоритм та динамічне програмування для вибору їжі.
    """
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    
    budget = int(input("Enter your budget: "))
    
    print("Greedy Algorithm Result:")
    greedy_result = greedy_algorithm(items, budget)
    print("Selected items:", greedy_result[0])
    print("Total calories:", greedy_result[1])
    print("Total cost:", greedy_result[2])
    
    print("\nDynamic Programming Result:")
    dp_result = dynamic_programming(items, budget)
    print("Selected items:", dp_result[0])
    print("Total calories:", dp_result[1])
    print("Total cost:", dp_result[2])

def task_7():
    """
    Виконує завдання 7: метод Монте-Карло для визначення ймовірностей сум при киданні двох кубиків.
    """
    run_monte_carlo_simulation()
