import tkinter as tk
from tkinter import messagebox
import heapq

class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        if to_node not in self.edges:
            self.edges[to_node] = []
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

def dijkstra(graph, start):
    """
    Реалізація алгоритму Дейкстри для знаходження найкоротших шляхів у зваженому графі.
    
    :param graph: об'єкт графа
    :param start: початкова вершина
    :return: відстані до всіх вершин від початкової вершини
    """
    if start not in graph.edges:
        raise KeyError(f"Start node {start} not in graph")

    shortest_paths = {vertex: float('infinity') for vertex in graph.edges}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > shortest_paths[current_vertex]:
            continue

        for neighbor in graph.edges[current_vertex]:
            weight = graph.weights.get((current_vertex, neighbor), float('infinity'))
            distance = current_distance + weight

            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths

class DijkstraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dijkstra's Algorithm")

        self.graph = Graph()

        self.edges_frame = tk.Frame(root)
        self.edges_frame.pack()

        self.start_label = tk.Label(self.edges_frame, text="Start Node:")
        self.start_label.grid(row=0, column=0)
        self.start_entry = tk.Entry(self.edges_frame)
        self.start_entry.grid(row=0, column=1)

        self.end_label = tk.Label(self.edges_frame, text="End Node:")
        self.end_label.grid(row=1, column=0)
        self.end_entry = tk.Entry(self.edges_frame)
        self.end_entry.grid(row=1, column=1)

        self.weight_label = tk.Label(self.edges_frame, text="Weight:")
        self.weight_label.grid(row=2, column=0)
        self.weight_entry = tk.Entry(self.edges_frame)
        self.weight_entry.grid(row=2, column=1)

        self.add_edge_button = tk.Button(self.edges_frame, text="Add Edge", command=self.add_edge)
        self.add_edge_button.grid(row=3, columnspan=2)

        self.run_dijkstra_frame = tk.Frame(root)
        self.run_dijkstra_frame.pack()

        self.start_node_label = tk.Label(self.run_dijkstra_frame, text="Start Node for Dijkstra:")
        self.start_node_label.grid(row=0, column=0)
        self.start_node_entry = tk.Entry(self.run_dijkstra_frame)
        self.start_node_entry.grid(row=0, column=1)

        self.run_button = tk.Button(self.run_dijkstra_frame, text="Run Dijkstra", command=self.run_dijkstra)
        self.run_button.grid(row=1, columnspan=2)

        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack()

    def add_edge(self):
        from_node = self.start_entry.get()
        to_node = self.end_entry.get()
        weight = self.weight_entry.get()

        if from_node and to_node and weight:
            try:
                weight = float(weight)
                self.graph.add_edge(from_node, to_node, weight)
                messagebox.showinfo("Success", f"Edge added: {from_node} -> {to_node} with weight {weight}")
                self.start_entry.delete(0, tk.END)
                self.end_entry.delete(0, tk.END)
                self.weight_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "Weight must be a number")
        else:
            messagebox.showerror("Error", "All fields must be filled")

    def run_dijkstra(self):
        start_node = self.start_node_entry.get()
        if start_node:
            try:
                shortest_paths = dijkstra(self.graph, start_node)
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, f"Shortest paths from node {start_node}:\n")
                for node, distance in shortest_paths.items():
                    self.result_text.insert(tk.END, f"Distance to {node}: {distance}\n")
            except KeyError as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Start node must be specified")

def run_dijkstra_app():
    root = tk.Tk()
    app = DijkstraApp(root)
    root.mainloop()
