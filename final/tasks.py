from linked_list import create_node, append, print_list, reverse, insertion_sort, merge_sorted_lists
from pythagoras_tree import draw_tree
from dijkstra_gui import run_dijkstra_app, generate_connected_random_graph
from dijkstra_visualization import visualize_graph
from dijkstra_gui import Graph, dijkstra

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
    draw_tree(level)

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
        print("Distance to {}: {}".format(node, distance))

    visualize_graph(graph, shortest_paths, start_node)

def task_4():
    """
    Виконує завдання 4: візуалізація графа та найкоротших шляхів.
    """
    run_dijkstra_app()
