import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import time

class Node:
    def __init__(self, key, color="skyblue"):
        """
        Ініціалізація вузла дерева.
        
        :param key: значення вузла
        :param color: колір вузла (за замовчуванням "skyblue")
        """
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """
    Додає ребра до графа для візуалізації дерева.
    
    :param graph: граф, що представляє дерево
    :param node: поточний вузол
    :param pos: позиції вузлів для візуалізації
    :param x: координата x поточного вузла
    :param y: координата y поточного вузла
    :param layer: поточний шар дерева
    :return: граф з доданими ребрами
    """
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree_with_colors(tree_root, node_colors, ax):
    """
    Малює дерево з кольоровими вузлами на основі заданих кольорів.
    
    :param tree_root: корінь дерева
    :param node_colors: словник кольорів для кожного вузла
    :param ax: візуалізаційна область Matplotlib
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node_colors.get(node[0], node[1]['color']) for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    ax.clear()
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, ax=ax)
    plt.draw()
    plt.pause(1)

def array_to_heap(array):
    """
    Перетворює масив у бінарну купу та повертає корінь дерева.
    
    :param array: масив значень
    :return: корінь дерева
    """
    if not array:
        return None

    nodes = [Node(key) for key in array]

    for i in range(len(array) // 2):
        if 2 * i + 1 < len(array):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(array):
            nodes[i].right = nodes[2 * i + 2]

    return nodes[0]

def generate_colors(n):
    """
    Генерує n кольорів від темних до світлих відтінків.
    
    :param n: кількість кольорів
    :return: список кольорів у 16-системі RGB
    """
    colors = []
    for i in range(n):
        value = int(255 * (i / (n - 1))) if n > 1 else 255
        colors.append(f'#{value:02X}{0:02X}{255 - value:02X}')
    return colors

def count_nodes(tree_root):
    """
    Рахує кількість вузлів у дереві.
    
    :param tree_root: корінь дерева
    :return: кількість вузлів
    """
    if tree_root is None:
        return 0
    queue = deque([tree_root])
    count = 0
    while queue:
        node = queue.popleft()
        count += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return count

def visualize_dfs(tree_root):
    """
    Візуалізує обхід дерева в глибину (DFS).
    
    :param tree_root: корінь дерева
    """
    if tree_root is None:
        return

    total_nodes = count_nodes(tree_root)
    colors = generate_colors(total_nodes)
    
    stack = [tree_root]
    node_colors = {}

    fig, ax = plt.subplots(figsize=(8, 5))
    plt.ion()  # Увімкнення інтерактивного режиму

    i = 0
    while stack:
        node = stack.pop()
        node_colors[node.id] = colors[i]
        i += 1
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        draw_tree_with_colors(tree_root, node_colors, ax)
    plt.ioff()  # Вимкнення інтерактивного режиму
    plt.show()

def visualize_bfs(tree_root):
    """
    Візуалізує обхід дерева в ширину (BFS).
    
    :param tree_root: корінь дерева
    """
    if tree_root is None:
        return

    total_nodes = count_nodes(tree_root)
    colors = generate_colors(total_nodes)
    
    queue = deque([tree_root])
    node_colors = {}

    fig, ax = plt.subplots(figsize=(8, 5))
    plt.ion()  # Увімкнення інтерактивного режиму

    i = 0
    while queue:
        node = queue.popleft()
        node_colors[node.id] = colors[i]
        i += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        draw_tree_with_colors(tree_root, node_colors, ax)
    plt.ioff()  # Вимкнення інтерактивного режиму
    plt.show()
