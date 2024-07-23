import matplotlib.pyplot as plt
import networkx as nx


class TreeNode:
    """
    Клас для вузла дерева.

    Атрибути:
    val: Значення ключа.
    left: Посилання на лівого нащадка.
    right: Посилання на правого нащадка.
    """

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    """
    Клас для двійкового дерева пошуку (BST).

    Атрибути:
    root: Корінь дерева.
    """

    def __init__(self):
        self.root = None

    def insert(self, key):
        """
        Вставка нового ключа в дерево.

        Аргументи:
        key: Значення ключа для вставки.
        """
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        """
        Допоміжний рекурсивний метод для вставки нового ключа в дерево.

        Аргументи:
        node: Поточний вузол дерева.
        key: Значення ключа для вставки.
        """
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)


def find_max_value(node):
    """
    Функція для знаходження найбільшого значення в дереві.

    Аргументи:
    node: Корінь дерева.

    Повертає:
    Найбільше значення в дереві.
    """
    current = node
    # Проходимо по правих піддеревах, поки не знайдемо найправіший вузол
    while current.right is not None:
        current = current.right
    return current.val


def visualize_tree(node):
    """
    Функція для візуалізації дерева за допомогою Matplotlib і NetworkX.

    Аргументи:
    node: Корінь дерева.
    """
    if node is None:
        return

    G = nx.DiGraph()
    pos = {}

    def add_edges(node, pos, x=0, y=0, layer=1):
        """
        Допоміжна функція для додавання вузлів і ребер до графу.

        Аргументи:
        node: Поточний вузол дерева.
        pos: Позиції вузлів.
        x: Позиція по осі X.
        y: Позиція по осі Y.
        layer: Поточний рівень дерева.
        """
        if node is not None:
            G.add_node(node.val, pos=(x, y))
            pos[node.val] = (x, y)
            if node.left:
                G.add_edge(node.val, node.left.val)
                add_edges(node.left, pos, x - 1 / layer, y - 1, layer + 1)
            if node.right:
                G.add_edge(node.val, node.right.val)
                add_edges(node.right, pos, x + 1 / layer, y - 1, layer + 1)

    add_edges(node, pos)
    nx.draw(G, pos, with_labels=True, arrows=False)
    plt.show()


